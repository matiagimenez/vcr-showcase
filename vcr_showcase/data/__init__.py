import json
from pathlib import Path
from typing import Any

from vcr_showcase.models import UserValidator


def load_json(path: Path) -> dict[str, Any]:
    with Path.open(path) as file:
        return json.load(file)


json_path = Path(__file__).parent / "data.json"
data = load_json(path=json_path)
USERS = UserValidator.validate_python(data)

__all__ = ["USERS"]
