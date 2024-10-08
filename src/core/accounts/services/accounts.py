from dataclasses import dataclass

from src.core.accounts.entities.dto import AccountRegistryDTO
from src.infra.db.models.accounts import Account
from src.infra.db.repositories.accounts import PostgresAccountsRepository


@dataclass
class AccountService:
    accounts: PostgresAccountsRepository

    async def create(self, data: AccountRegistryDTO) -> Account:
        return await self.accounts.create_account(data.type)
