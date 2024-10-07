import pytest

from infra.db.models.users import User
from infra.db.repositories.users import PostgresUsersRepository


@pytest.mark.asyncio
async def test_insert_user():
    repo = PostgresUsersRepository()
    user = User(name="John", document="48558362068")
    result = await repo.insert(user)
    assert result is not None
    assert result.id is not None
    assert result.name == user.name
    assert result.document == user.document
