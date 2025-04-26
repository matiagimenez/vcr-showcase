from uuid import UUID
from fastapi import APIRouter, status, HTTPException
from vcr_showcase.data import USERS
from vcr_showcase.models import User

router = APIRouter(prefix="/api/users")


@router.get("/")
def get_all_users() -> list[User]:
    return USERS


@router.get("/{user_id}")
def get_user(user_id: UUID) -> User:
    user = next((user for user in USERS if user.id_ == user_id), None)
    if not user:
        exception = f"User not found withg id {user_id}"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exception)
    return user
