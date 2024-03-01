from fastapi import FastAPI
from starlette.responses import Response


def create_http_controller() -> FastAPI:
    api = FastAPI()

    @api.get("/health")
    def health() -> Response:
        return Response("OK")

    return api
