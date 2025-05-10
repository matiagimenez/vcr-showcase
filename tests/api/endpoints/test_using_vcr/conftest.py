from typing import Any
import pytest
from .helper import sanitize_response, sanitize_request


@pytest.fixture(scope="module", autouse=True)
def vcr_config() -> dict[str, Any]:
    return {
        "filter_headers": ["authorization"],
        "record_mode": "once",
        "before_record_response": [sanitize_response],
        "before_record_request": [sanitize_request],
    }
