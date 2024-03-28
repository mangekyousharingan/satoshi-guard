from fastapi import FastAPI
from starlette.responses import JSONResponse


def create_http_controller() -> FastAPI:
    controller = FastAPI()

    @controller.get("/health")
    def health() -> JSONResponse:
        return JSONResponse({"status": "OK"})

    return controller
