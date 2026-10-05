"""Сборка HTTP-приложения и его зависимостей."""

from fastapi import FastAPI

from locate import __version__
from locate.presentation.api.routes import router

_API_TITLE = "Locate API"


def create_app() -> FastAPI:
    app = FastAPI(title=_API_TITLE, version=__version__)
    app.include_router(router)
    return app
