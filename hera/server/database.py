import os

from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from dotenv import load_dotenv

load_dotenv()

POSTGRES_URL = os.getenv("POSTGRES_URL")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASS = os.getenv("POSTGRES_PASS")
POSTGRES_DB = os.getenv("POSTGRES_DB")

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_URL}/{POSTGRES_DB}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args={ "timeout": 10 })

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

meta = MetaData(schema="star")
Base = declarative_base(metadata=meta)

async def get_db() -> AsyncSession:

    async with SessionLocal() as session:
        yield session
