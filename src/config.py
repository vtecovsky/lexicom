from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env.local"
        env_file_encoding = "utf-8"

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int


settings = Settings()
