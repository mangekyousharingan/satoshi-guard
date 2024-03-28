from abc import ABC, abstractmethod

from src.config.models import HttpServer


class AbstractConfig(ABC):

    @abstractmethod
    def http_server(self) -> HttpServer:
        raise NotImplemented
