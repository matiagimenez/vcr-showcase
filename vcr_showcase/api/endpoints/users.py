from typing import Any
from uuid import UUID
from fastapi import APIRouter
from vcr_showcase.models import User, UserList, LoginInformation
import requests

from vcr_showcase.settings import Settings

router = APIRouter(prefix="/api/users")


@router.get("/")
def get_all_users() -> list[User]:
    response = requests.get(f"{Settings.API_URL}/users")
    users = response.json().get("users", [])
    return UserList.validate_python(users)


@router.get("/{user_id}")
def get_user(user_id: int) -> User:
    response = requests.get(f"{Settings.API_URL}/users/{user_id}")
    user = response.json()
    return User.model_validate(user)


@router.post("/login")
def login(login_information: LoginInformation) -> Any:
    data = login_information.model_dump()
    response = requests.post(f"{Settings.API_URL}/user/login", json=data)
    return response.json()
