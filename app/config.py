from pydantic import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    db_url: str = os.getenv("MONGO_URL", "")
    db_name: str = os.getenv("MONGO_DB", "")
    collection: str = os.getenv("MONGO_COLLECTION", "")
    collection2: str = os.getenv("MONGO_COLLECTION2", "")
    client_origin: str = os.getenv("CLIENT_ORIGIN", "")







@lru_cache
def get_settings():
    return Settings()