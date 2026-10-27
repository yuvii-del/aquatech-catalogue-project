
from pydantic import BaseModel, ConfigDict, Field


class BrandOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    slug: str
    description: str
    logo_url: str | None = None


class CategoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    slug: str
    description: str


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=180)
    slug: str = Field(min_length=1, max_length=200)
    model_number: str = Field(default="", max_length=120)
    description: str = ""
    image_url: str = Field(default="", max_length=1000)
    mrp: int | None = Field(default=None, ge=0)
    featured: bool = False
    brand_id: int
    category_id: int
    highlights: list[str] = Field(default_factory=list)
    specifications: list[dict] = Field(default_factory=list)
    features: list[dict] = Field(default_factory=list)


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=180)
    slug: str | None = Field(default=None, min_length=1, max_length=200)
    model_number: str | None = Field(default=None, max_length=120)
    description: str | None = None
    image_url: str | None = Field(default=None, max_length=1000)
    mrp: int | None = Field(default=None, ge=0)
    featured: bool | None = None
    brand_id: int | None = None
    category_id: int | None = None
    highlights: list[str] | None = None
    specifications: list[dict] | None = None
    features: list[dict] | None = None


class ProductOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    slug: str
    model_number: str
    description: str
    image_url: str
    mrp: int | None
    featured: bool
    brand: BrandOut
    category: CategoryOut
    highlights: list[str] = Field(default_factory=list)
    specifications: list[dict] = Field(default_factory=list)
    features: list[dict] = Field(default_factory=list)
