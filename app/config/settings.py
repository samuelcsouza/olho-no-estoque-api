import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE")


def get_settings() -> Settings:
    return Settings()
