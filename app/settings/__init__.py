from os import getenv
from pathlib import Path
from typing import Optional, Tuple, Type

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    YamlConfigSettingsSource,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

env = getenv("ENV", "dev")
ROOT_DIR = Path(__file__).parent


class AppConfig(BaseModel):
    name: str
    version: str
    debug: bool = False
    log_level: str = "info"


class Settings(BaseSettings):
    database_url: Optional[str] = getenv("DATABASE_URL")
    app: AppConfig

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        default_settings = [
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
        ]

        base_yaml = Path(ROOT_DIR, "./base.yaml")
        if base_yaml.exists():
            default_settings.append(YamlConfigSettingsSource(settings_cls, base_yaml))

        env_yaml = Path(ROOT_DIR, f"./{env}.yaml")
        if env_yaml.exists():
            default_settings.append(YamlConfigSettingsSource(settings_cls, env_yaml))

        return tuple(default_settings)


setting = Settings()

# SQLAlchemy 엔진 생성
engine = create_engine(setting.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
