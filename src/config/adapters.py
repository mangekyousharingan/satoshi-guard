import sys

import yaml

from src.config.models import Database, HttpServer
from src.config.ports import AbstractConfig


class YAMLConfig(AbstractConfig):
    def __init__(self, config_path: str) -> None:
        self._config_file = self._read_config(config_path)

    def _read_config(self, config_path: str):
        with open(config_path) as stream:
            try:
                config_file = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                sys.exit(1)
            finally:
                return config_file

    @property
    def http_server(self) -> HttpServer:
        return HttpServer(
            host=self._config_file["http_server"]["host"], port=self._config_file["http_server"]["port"]
        )

    @property
    def database(self) -> Database:
        return Database(
            host=self._config_file["database"]["host"],
            port=self._config_file["database"]["port"],
            username=self._config_file["database"]["username"],
            password=self._config_file["database"]["password"],
            db_name=self._config_file["database"]["db_name"],
        )
