from typing import Any
from fastapi.testclient import TestClient
from fastapi import status
import pytest
from vcr_showcase.models import UserLoginInformation


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
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == user_as_dict


@pytest.mark.usefixtures("_patch_user_login")
def test_login(
    test_client: TestClient, login_information: UserLoginInformation
) -> None:
    response = test_client.post("/api/users/login", json=login_information.model_dump())
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("accessToken")
