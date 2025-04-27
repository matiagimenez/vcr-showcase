from fastapi.testclient import TestClient
from fastapi import status


def test_status(test_client: TestClient) -> None:
    response = test_client.get("/api/status")
    assert response.status_code == status.HTTP_200_OK
