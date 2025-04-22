from uuid import UUID

from fastapi import APIRouter

from vcr_showcase.data import USERS
from vcr_showcase.models import User

from .helper import get_user_by_id

router = APIRouter(prefix="/api/users")


@router.get("/")
def get_all_users() -> list[User]:
    return USERS


@router.get("/{user_id}")
def get_user(user_id: UUID) -> User:
    return get_user_by_id(user_id=user_id)
