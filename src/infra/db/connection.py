from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.environment import settings

engine = create_async_engine(str(settings.POSTGRES_URI), echo=True)


class AsyncDBSessionsManager:
    session: AsyncSession

    async def __aenter__(self) -> "AsyncDBSessionsManager":
        self.session = AsyncSession(engine, expire_on_commit=False)
        return self

    async def __aexit__(self, *args) -> None:
        await self.session.close()
