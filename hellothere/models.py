from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    func,
)


Base = declarative_base(metadata=MetaData())


class Name(Base):
    __tablename__ = "name"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(250), nullable=False)

    first_insert = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    last_insert = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    def __repr__(self):
        return f"Name(name={self.name}, first_insert={self.first_insert}, " \
               f"last_insert=self.last_insert)"
