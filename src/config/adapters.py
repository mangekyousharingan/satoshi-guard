from src.config.models import HttpServer
from src.config.ports import AbstractConfig
import yaml


class YAMLConfig(AbstractConfig):
    def __init__(self, config_file: str) -> str:
        self._config_file = self._config_path(config_file)

    def _config_path(self, config_file: str) -> str:
        return f"src/config/files/{config_file}.yaml"

    def _read_config(self):
        # TODO: read config
        pass

    @property
    def http_server(self) -> HttpServer:
        # TODO: read from file
        return HttpServer(host="0.0.0.0", port=8080)
