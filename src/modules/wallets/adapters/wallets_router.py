from fastapi import APIRouter
from starlette.responses import JSONResponse

wallets_router = APIRouter()


@wallets_router.get("/")
def wallets_router() -> JSONResponse:
    return JSONResponse({"router": "wallets"})
