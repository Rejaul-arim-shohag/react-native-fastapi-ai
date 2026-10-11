from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.endpoints import auth, health
from app.db.base import Base
from app.db.session import engine
from app.models.user import User  # Registers the User table


@asynccontextmanager
async def lifespan(app: FastAPI):
    # For initial local development only.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="AI Chat API", lifespan=lifespan)

app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
