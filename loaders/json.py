import logging
from pathlib import Path

from pydantic import BaseModel
from pydantic_loader import CfgError, load_json

from loaders.base import BaseConfigLoader
from models import Citizen, Config, Role

logger = logging.getLogger(__name__)


class LoadedConfig(BaseModel):
    citizens: list[Citizen]
    roles: list[Role]


class JsonConfigLoader(BaseConfigLoader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def load_config(self, path: str) -> Config:
        try:
            config = load_json(LoadedConfig, Path(path))
            return Config(
                citizens={c.name: c for c in config.citizens},
                roles={r.title: r for r in config.roles},
            )
        except CfgError as e:
            logger.error("Config file is not valid: %s", e)
            raise e from None
