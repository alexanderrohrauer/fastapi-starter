from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.settings import get_settings, Env
from app.middlewares import cors_middleware


@asynccontextmanager
async def lifespan(app_: FastAPI):
    # Code before the app starts
    yield
    # Code when the app gets the shutdown


settings = get_settings()

docs_url = None if settings.env == Env.PRODUCTION else "/docs"
redoc_url = None if settings.env == Env.PRODUCTION else "/redoc"
openapi_url = None if settings.env == Env.PRODUCTION else "/openapi.json"

app = FastAPI(
    lifespan=lifespan, docs_url=docs_url, redoc_url=redoc_url, openapi_url=openapi_url
)

cors_middleware.add(app)
