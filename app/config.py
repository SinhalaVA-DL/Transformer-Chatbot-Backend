from pydantic.v1 import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    db_url: str = os.getenv("MONGO_URL", "")
    db_name: str = os.getenv("MONGO_DB", "")
    collection: str = os.getenv("MONGO_COLLECTION", "")
    collection2: str = os.getenv("MONGO_COLLECTION2", "")
    client_origin: str = os.getenv("CLIENT_ORIGIN", "")
    weather_apiKey: str = os.getenv("OPEN_WEATHER_API_KEY", "")

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
