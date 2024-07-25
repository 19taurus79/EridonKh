from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    db_name: str = Field(env="DB_NAME")
    db_user: str = Field(env="DB_USER")
    db_password: str = Field(env="DB_PASSWORD")
    db_host: str = Field(env="DB_HOST")
    db_port: int = Field(env="DB_PORT")
    secret_key: str = Field(env="SECRET_KEY")
    debug: bool = Field(env="DEBUG")
    django_allowed_hosts: str = Field(env="DJANGO_ALLOWED_HOST")


settings = Settings()
