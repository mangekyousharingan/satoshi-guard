from dataclasses import dataclass
from enum import StrEnum, Enum


@dataclass
class HttpServer:
    host: str
    port: int
