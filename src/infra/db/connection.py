from contextlib import asynccontextmanager

import databases

from src.config.environment import settings

database = databases.Database(str(settings.POSTGRES_URI))


@asynccontextmanager
async def database_context():
    await connect_database()
    yield database
    await disconnect_database()


async def connect_database():
    await database.connect()


async def disconnect_database():
    await database.disconnect()
