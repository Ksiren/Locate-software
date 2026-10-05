"""Схемы HTTP-ответов."""

from enum import StrEnum

from pydantic import BaseModel


class HealthStatus(StrEnum):
    OK = "ok"


class HealthResponse(BaseModel):
    status: HealthStatus = HealthStatus.OK
