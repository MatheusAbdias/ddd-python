__all__ = ["start_web_server"]

import uvicorn

from src.api import create_app

web_app = create_app()


def start_web_server() -> None:
    uvicorn.run(web_app)
