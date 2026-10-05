"""Проверка работоспособности HTTP-сервиса."""

from fastapi import APIRouter

from locate.presentation.api.schemas import HealthResponse

_HEALTH_PATH = "/health"
_HEALTH_TAG = "health"

router = APIRouter()


@router.get(_HEALTH_PATH, response_model=HealthResponse, tags=[_HEALTH_TAG])
def health() -> HealthResponse:
    return HealthResponse()
