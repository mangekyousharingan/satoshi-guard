import uvicorn

from src.controller.http import create_http_controller


class SatoshiGuard:
    def __init__(self, port: int, host: str) -> None:
        self.port = port
        self.host = host

    def start_service(self) -> None:
        http_controller = create_http_controller()

        uvicorn.run(http_controller, port=self.port, host=self.host)
