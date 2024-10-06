from dataclasses import dataclass

from src.infra.db.models.accounts import Account, AccountType
from src.infra.db.repositories.base import PostgresRepository


@dataclass
class PostgresAccountsRepository(PostgresRepository[Account]):
    model = Account

    async def create_account(
        self,
        type: AccountType,
        branch: str,
        number: str,
    ) -> Account:
        account = Account(type=type, branch=branch, number=number)
        return await self.insert(account)
