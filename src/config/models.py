from dataclasses import dataclass


@dataclass
class HttpServer:
    host: str
    port: int
