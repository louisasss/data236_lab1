from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str = "yelpclone"
    db_user: str = "root"
    db_password: str = ""

    # JWT
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24  # 24 hours

    # AI
    openai_api_key: str = ""
    tavily_api_key: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
