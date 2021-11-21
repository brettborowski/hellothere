import os

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv

load_dotenv(".env")
SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")

engine = create_engine(
    SQLALCHEMY_DATABASE_URI  # , connect_args={"check_same_thread}": False}
)
metadata = MetaData()
LocalSession = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


def init_db():
    metadata.create_all(bind=engine)
