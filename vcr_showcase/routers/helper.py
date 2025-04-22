from uuid import UUID

from fastapi import HTTPException

from vcr_showcase.data import USERS
from vcr_showcase.models import User


def get_user_by_id(user_id: UUID) -> User:
    user = next((user for user in USERS if user.id_ == user_id), None)
    if not user:
        raise HTTPException(
            status_code=404, detail=f"User not found withg id {user_id}"
        )
    return user
