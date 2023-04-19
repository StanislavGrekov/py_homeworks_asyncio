from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import JSON, Integer, Column


PG_DSN = 'postgresql+asyncpg://postgres:masterkey@127.0.0.1:5431/my_db'
engine = create_async_engine(PG_DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class SwapiPeople(Base):

    __tablename__ = 'swapi_people'
    id = Column(Integer, primary_key=True)
    json = Column(JSON)