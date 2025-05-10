from fastapi.testclient import TestClient
from fastapi import status
import pytest
from vcr_showcase.models import User, UserList, UserLoginInformation


@pytest.mark.vcr
def test_get_all_users(test_client: TestClient) -> None:
    response = test_client.get("/api/users/")
    assert response.status_code == status.HTTP_200_OK
    assert UserList.validate_python(response.json())


@pytest.mark.vcr
def test_get_user_by_id(test_client: TestClient, user_id: int) -> None:
    response = test_client.get(f"/api/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK
    assert User.model_validate(response.json())


@pytest.mark.vcr
def test_login(
    test_client: TestClient, login_information: UserLoginInformation
) -> None:
    response = test_client.post("/api/users/login", json=login_information.model_dump())
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("accessToken")
