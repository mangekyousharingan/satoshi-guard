import argparse

from src.app import SatoshiGuard
from src.config.adapters import YAMLConfig


def parse_command_line_args() -> argparse.Namespace:
    available_config_files = ["local"]
    parser = argparse.ArgumentParser(description="scanner-service application")
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="name of the configuration file inside the src.configs.files module",
        choices=available_config_files,
    )

    args = parser.parse_args()

    return args


def main() -> None:
    args = parse_command_line_args()
    config = YAMLConfig(args.config)
    satoshi_guard = SatoshiGuard(port=config.http_server.port, host=config.http_server.host)
    satoshi_guard.start_service()


if __name__ == '__main__':
    main()
