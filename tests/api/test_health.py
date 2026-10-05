from http import HTTPStatus

from fastapi.testclient import TestClient

from locate.bootstrap import create_app

_HEALTH_PATH = "/health"
_EXPECTED_BODY = {"status": "ok"}
_CONTENT_TYPE_HEADER = "content-type"
_JSON_CONTENT_TYPE = "application/json"


def test_health_returns_ok() -> None:
    with TestClient(create_app()) as client:
        response = client.get(_HEALTH_PATH)

    assert response.status_code == HTTPStatus.OK
    assert response.headers[_CONTENT_TYPE_HEADER] == _JSON_CONTENT_TYPE
    assert response.json() == _EXPECTED_BODY
