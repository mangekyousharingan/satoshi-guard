from typing import Any

from src.config.models import HttpServer
from src.config.port import AbstractConfig


class ConfigAdapter(AbstractConfig):
    def __init__(self, config_file: Any) -> None:
        self._config_file = config_file

    @property
    def http_server(self) -> HttpServer:
        return HttpServer(
            host=self._config_file["http_server"]["host"], port=self._config_file["http_server"]["port"]
        )
