from fastapi import FastAPI

from api.routes import register_routers


def create_app() -> FastAPI:
    app = FastAPI()
    register_routers(app)

    return app
