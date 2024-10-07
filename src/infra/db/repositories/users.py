from dataclasses import dataclass

from infra.db.models.users import User
from infra.db.repositories.base import PostgresRepository


@dataclass
class PostgresUsersRepository(PostgresRepository[User]):
    model = User

    async def create_user(self, name: str, document: str) -> User:
        user = User(name=name, document=document)
        return await self.insert(user)
