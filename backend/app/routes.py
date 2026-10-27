
import logging

from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy import or_, select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app.models import Brand, Category, Product
from app.schemas import (
    BrandOut,
    CategoryOut,
    ProductCreate,
    ProductOut,
    ProductUpdate,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api")


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/brands", response_model=list[BrandOut])
def list_brands(db: Session = Depends(get_db)):
    try:
        stmt = select(Brand).order_by(Brand.name)
        return list(db.scalars(stmt).all())
    except SQLAlchemyError:
        logger.exception("Failed to fetch brands")
        raise HTTPException(
            status_code=500,
            detail="Unable to fetch brands.",
        )


@router.get("/categories", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    try:
        stmt = select(Category).order_by(Category.name)
        return list(db.scalars(stmt).all())
    except SQLAlchemyError:
        logger.exception("Failed to fetch categories")
        raise HTTPException(
            status_code=500,
            detail="Unable to fetch categories.",
        )


@router.get("/products", response_model=list[ProductOut])
def list_products(
    search: str | None = Query(default=None, max_length=100),
    brand: str | None = Query(default=None, max_length=140),
    category: str | None = Query(default=None, max_length=140),
    featured: bool | None = None,
    db: Session = Depends(get_db),
):
    try:
        stmt = select(Product).options(
            joinedload(Product.brand),
            joinedload(Product.category),
        )

        if search and search.strip():
            term = f"%{search.strip()}%"
            stmt = stmt.where(
                or_(
                    Product.name.ilike(term),
                    Product.model_number.ilike(term),
                    Product.description.ilike(term),
                )
            )

        if brand:
            stmt = stmt.join(Product.brand).where(
                Brand.slug == brand
            )

        if category:
            stmt = stmt.join(Product.category).where(
                Category.slug == category
            )

        if featured is not None:
            stmt = stmt.where(Product.featured == featured)

        stmt = stmt.order_by(Product.name)

        return list(db.scalars(stmt).unique().all())

    except SQLAlchemyError:
        logger.exception("Failed to fetch products")
        raise HTTPException(
            status_code=500,
            detail="Unable to fetch products.",
        )


@router.get("/products/{slug}", response_model=ProductOut)
def get_product(
    slug: str,
    db: Session = Depends(get_db),
):
    try:
        stmt = (
            select(Product)
            .options(
                joinedload(Product.brand),
                joinedload(Product.category),
            )
            .where(Product.slug == slug)
        )
        logger.info("Looking up product slug: %r", slug)
        logger.info("Database URL configured: %s", "check your active database connection")
        product = db.scalars(stmt).first()
        logger.info("Product found: %s", product.name if product else "NO MATCH")
        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found.",
            )

        return product

    except HTTPException:
        raise
    except SQLAlchemyError:
        logger.exception("Failed to fetch product: %s", slug)
        raise HTTPException(
            status_code=500,
            detail="Unable to fetch product.",
        )


@router.post(
    "/products",
    response_model=ProductOut,
    status_code=201,
)
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
):
    if db.get(Brand, data.brand_id) is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid brand ID.",
        )

    if db.get(Category, data.category_id) is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid category ID.",
        )

    product = Product(**data.model_dump())
    db.add(product)

    try:
        db.commit()
        db.refresh(product)

        # Load relationships needed by ProductOut.
        db.refresh(product, attribute_names=["brand", "category"])
        return product

    except IntegrityError:
        db.rollback()
        logger.exception("Product creation failed due to a constraint")
        raise HTTPException(
            status_code=409,
            detail="A product with a conflicting unique value already exists.",
        )
    except SQLAlchemyError:
        db.rollback()
        logger.exception("Failed to create product")
        raise HTTPException(
            status_code=500,
            detail="Unable to create product.",
        )


@router.put(
    "/products/{product_id}",
    response_model=ProductOut,
)
def replace_product(
    product_id: int,
    data: ProductCreate,
    db: Session = Depends(get_db),
):
    """Replace all editable product fields."""
    product = db.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found.",
        )

    if db.get(Brand, data.brand_id) is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid brand ID.",
        )

    if db.get(Category, data.category_id) is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid category ID.",
        )

    for field, value in data.model_dump().items():
        setattr(product, field, value)

    try:
        db.commit()
        db.refresh(product)
        return product

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A product with a conflicting unique value already exists.",
        )
    except SQLAlchemyError:
        db.rollback()
        logger.exception("Failed to replace product %s", product_id)
        raise HTTPException(
            status_code=500,
            detail="Unable to update product.",
        )


@router.patch(
    "/products/{product_id}",
    response_model=ProductOut,
)
def update_product(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db),
):
    """Update only the fields supplied by the caller."""
    product = db.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found.",
        )

    changes = data.model_dump(exclude_unset=True)

    if "brand_id" in changes:
        if changes["brand_id"] is None:
            raise HTTPException(
                status_code=400,
                detail="Brand ID cannot be null.",
            )
        if db.get(Brand, changes["brand_id"]) is None:
            raise HTTPException(
                status_code=400,
                detail="Invalid brand ID.",
            )

    if "category_id" in changes:
        if changes["category_id"] is None:
            raise HTTPException(
                status_code=400,
                detail="Category ID cannot be null.",
            )
        if db.get(Category, changes["category_id"]) is None:
            raise HTTPException(
                status_code=400,
                detail="Invalid category ID.",
            )

    for field, value in changes.items():
        setattr(product, field, value)

    try:
        db.commit()
        db.refresh(product)

        # Load updated relationships for the response.
        db.refresh(product, attribute_names=["brand", "category"])
        return product

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A product with a conflicting unique value already exists.",
        )
    except SQLAlchemyError:
        db.rollback()
        logger.exception("Failed to update product %s", product_id)
        raise HTTPException(
            status_code=500,
            detail="Unable to update product.",
        )


@router.delete(
    "/products/{product_id}",
    status_code=204,
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = db.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found.",
        )

    try:
        db.delete(product)
        db.commit()
        return Response(status_code=204)

    except SQLAlchemyError:
        db.rollback()
        logger.exception("Failed to delete product %s", product_id)
        raise HTTPException(
            status_code=500,
            detail="Unable to delete product.",
        )
