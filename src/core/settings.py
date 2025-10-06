# src/core/settings.py
from typing import Literal, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = Field("UrbanPlannerMCP", alias="APP_NAME")
    stateless_http: bool = Field(True, alias="STATELESS_HTTP")
    transport: Literal["stdio", "streamable-http"] = Field("streamable-http", alias="TRANSPORT_METHOD")

    google_maps_api_key: Optional[str] = Field(None, alias="GOOGLE_MAPS_API")
    infra_model_host: Optional[str] = Field(None, alias="INFRA_MODEL_HOST")
    population_model_host: Optional[str] = Field(None, alias="POPULATION_MODEL_HOST")

@lru_cache
def get_settings() -> "Settings":
    return Settings()
