from dataclasses import dataclass


@dataclass
class HttpServer:
    host: str
    port: int


@dataclass
class Database:
    host: str
    port: int
    username: str
    password: str
    db_name: str

    @property
    def connection_url(self):
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"
