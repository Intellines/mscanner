from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    API_ID: int
    API_HASH: str

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


config: Config = Config()
