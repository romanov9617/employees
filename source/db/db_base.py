from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config import settings

class Base(DeclarativeBase):
    pass


engine = create_async_engine(settings.DB_URL)

async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

# async def create_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# async def get_db():
#     try:
#         async with async_session() as db:
#             yield db
#     finally:
#         await engine.dispose()
