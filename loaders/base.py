import abc

from models import Config


class BaseConfigLoader(abc.ABC):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @abc.abstractmethod
    def load_config(self, path: str) -> Config:
        ...
