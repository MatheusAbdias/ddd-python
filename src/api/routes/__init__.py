from fastapi.applications import FastAPI

from src.api.routes import accounts


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(accounts.router, prefix="/accounts")
    return app
