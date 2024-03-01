from typing import Any

import uvicorn
import yaml

from src.config.adapters.config import ConfigAdapter
from src.controllers.http import create_http_controller


def config_path() -> str:
    return "src/config/files/local.yml"


def read_config_file(path: str) -> Any:
    with open(path) as file:
        config_file = yaml.safe_load(file)
    return config_file


def main() -> None:
    config = ConfigAdapter(read_config_file(config_path()))
    http_controller = create_http_controller()
    uvicorn.run(http_controller, host=config.http_server.host, port=config.http_server.port)


if __name__ == "__main__":
    main()
