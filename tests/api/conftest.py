from fastapi.testclient import TestClient
import pytest

from vcr_showcase.main import app


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    return TestClient(app)
