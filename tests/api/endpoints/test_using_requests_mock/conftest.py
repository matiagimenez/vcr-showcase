from typing import Any, Generator
from unittest.mock import MagicMock, patch
import pytest
from requests_mock import Mocker
from vcr_showcase.settings import Settings


@pytest.fixture
def _patch_get_user_by_id(
    user_id: int,
    user_as_dict: dict[str, Any],
    requests_mock: Mocker,
) -> Generator[None, None, None]:
    url = f"{Settings.API_URL}/users/{user_id}"
    requests_mock.get(url, json=user_as_dict)
    yield


@pytest.fixture
def _patch_get_users(
    many_users_as_dict: dict[str, Any],
    requests_mock: Mocker,

) -> Generator[None, None, None]:
    url = f"{Settings.API_URL}/users"
    requests_mock.get(url, json={"users": many_users_as_dict})
    yield
