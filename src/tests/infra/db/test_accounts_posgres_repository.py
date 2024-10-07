import pytest

from infra.db.models.accounts import Account, AccountType
from infra.db.repositories.accounts import PostgresAccountsRepository


@pytest.mark.asyncio
async def test_insert_account():
    repo = PostgresAccountsRepository()
    account = Account(type=AccountType.PERSONAL, branch="0001", number="123456")

    result = await repo.insert(account)

    assert result is not None
    assert result.id is not None
    assert result.type == account.type
    assert result.branch == account.branch
    assert result.number == account.number
    assert result.balance == 0
    assert result.created_at is not None
    assert result.updated_at is not None
