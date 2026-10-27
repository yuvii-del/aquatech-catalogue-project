
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import FRONTEND_ORIGIN
from app.database import Base, SessionLocal, engine
from app import models
from app.routes import router
from app.seed import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables from registered SQLAlchemy models.
    Base.metadata.create_all(bind=engine)

    # Insert initial catalogue data.
    with SessionLocal() as db:
        seed_database(db)

    yield


app = FastAPI(
    title="AquaTech Catalogue API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],
    allow_credentials=False,
    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
        "OPTIONS",
    ],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "name": "AquaTech Catalogue API",
        "docs": "/docs",
        "health": "/api/health",
    }
