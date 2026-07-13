"""
Application configuration loaded from environment variables.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Augment Knowledge Workspace"
    ENVIRONMENT: str = "development"

    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/augment_kw"

    # Auth
    SECRET_KEY: str = "change-me-in-env"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # LLM / AI (Milestone 3)
    OPENROUTER_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    LLM_MODEL: str = "gpt-4o-mini"

    class Config:
        env_file = ".env"


settings = Settings()
