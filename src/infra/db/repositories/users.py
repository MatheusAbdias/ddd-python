from src.infra.db.models.users import User
from src.infra.db.repositories.base import PostgresRepository


class PostgresUsersRepository(PostgresRepository[User]):
    def __init__(self):
        super().__init__(User)

    async def create_user(self, first_name: str, last_name: str, age: int) -> User:
        user = User(first_name=first_name, last_name=last_name, age=age)
        return await self.insert(user)
