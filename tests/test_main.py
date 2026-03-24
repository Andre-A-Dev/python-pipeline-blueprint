from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_convert():
    response = client.post("/convert", json={"key": "value"})
    assert response.status_code == 200
    assert response.json()["converted"] is True