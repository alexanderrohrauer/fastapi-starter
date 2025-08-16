from contextlib import asynccontextmanager

from app.middlewares import cors_middleware
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app_: FastAPI):
    # Code before the app starts
    yield
    # Code when the app gets the shutdown

app = FastAPI(lifespan=lifespan)

cors_middleware.add(app)
