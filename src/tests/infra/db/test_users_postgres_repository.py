import pytest

from src.infra.db.models.users import User
from src.infra.db.repositories.users import PostgresUsersRepository


@pytest.mark.asyncio
async def test_insert_user():
    repo = PostgresUsersRepository()
    user = User(first_name="John", last_name="Doe", age=30)

    result = await repo.insert(user)
    assert result is not None
    assert result.id is not None
    assert result.first_name == user.first_name
    assert result.last_name == user.last_name
    assert result.age == user.age
