import uuid

from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import UUIDType

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
