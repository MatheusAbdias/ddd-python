from dataclasses import dataclass

from src.core.accounts.entities.enums import AccountType
from src.infra.db.models.accounts import Account
from src.infra.db.repositories.base import PostgresRepository


@dataclass
class PostgresAccountsRepository(PostgresRepository[Account]):
    model = Account

    async def create_account(self, type: AccountType) -> Account:
        account = Account(type=type)

        return await self.insert(account)
