import logging
from typing import Generic, TypeVar

from sqlmodel import select

from src.infra.db.connection import AsyncDBSessionsManager
from src.infra.db.models.base import Model

T = TypeVar("T", bound=Model)

logger = logging.getLogger(__name__)


class PostgresRepository(Generic[T]):
    model: type[T]

    async def insert(self, model_instance: T) -> T:
        async with AsyncDBSessionsManager() as database:
            try:
                database.session.add(model_instance)
                await database.session.commit()
                await database.session.refresh(model_instance)
                return model_instance
            except Exception as e:
                await database.session.rollback()
                logger.exception(e)
                raise e

    async def get_by_id(self, model_id: int) -> T | None:
        async with AsyncDBSessionsManager() as database:
            query = select(self.model).where(self.model.id == model_id)
            result = await database.session.exec(query)
            return result.one_or_none()
