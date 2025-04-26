from vcr_showcase.main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    return TestClient(app)
