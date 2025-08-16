from enum import Enum
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Env(Enum):
    DEVELOPMENT = "DEVELOPMENT"
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    env: Env = Env.DEVELOPMENT

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()
