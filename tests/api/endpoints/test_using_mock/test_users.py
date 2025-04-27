from typing import Any
import pytest
from fastapi.testclient import TestClient
from fastapi import status


@pytest.mark.usefixtures("_patch_get_users")
def test_get_all_users(
    test_client: TestClient, many_users_as_dict: dict[str, Any]
) -> None:
    response = test_client.get("/api/users/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == many_users_as_dict


@pytest.mark.usefixtures("_patch_get_user_by_id")
def test_get_user_by_id(
    test_client: TestClient, user_id: int, user_as_dict: dict[str, Any]
) -> None:
    response = test_client.get(f"/api/users/{user_id}")
    print(f"response: {response.json()}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == user_as_dict
