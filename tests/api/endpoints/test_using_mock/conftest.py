from unittest.mock import MagicMock, patch

import pytest
from typing import Any, Generator


@pytest.fixture
def _patch_get_user_by_id(user_as_dict: dict[str, Any]) -> Generator[MagicMock, None, None]:
    with patch("vcr_showcase.api.endpoints.users.requests.get") as mock_requests_get:
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = user_as_dict
        yield mock_requests_get


@pytest.fixture
def _patch_get_users(many_users_as_dict: dict[str, Any]) -> Generator[MagicMock, None, None]:
    with patch("vcr_showcase.api.endpoints.users.requests.get") as mock_requests_get:
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {
            "users": many_users_as_dict}
        yield mock_requests_get
