from abc import ABC, abstractmethod

from src.config.models import HttpServer


class AbstractConfig(ABC):
    @property
    @abstractmethod
    def http_server(self) -> HttpServer:
        raise NotImplementedError
