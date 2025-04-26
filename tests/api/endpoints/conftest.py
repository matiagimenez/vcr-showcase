from vcr_showcase.models import User, UserList
import pytest
from typing import Any
from polyfactory.factories.pydantic_factory import ModelFactory
from polyfactory.pytest_plugin import register_fixture


@register_fixture(name="user_factory")
class UserFactory(ModelFactory[User]):
    ...


@pytest.fixture
def user_id() -> int:
    return 1


@pytest.fixture
def user(user_factory: ModelFactory[User], user_id: int) -> User:
    return user_factory.build(id=user_id)


@pytest.fixture
def many_users(user_factory: ModelFactory[User]) -> list[User]:
    return [user_factory.build() for _ in range(1, 3)]


@pytest.fixture
def user_as_dict(user: User) -> dict[str, Any]:
    return user.model_dump(by_alias=True)


@pytest.fixture
def many_users_as_dict(many_users: list[User]) -> dict[str, Any]:
    return UserList.dump_python(many_users, by_alias=True)
