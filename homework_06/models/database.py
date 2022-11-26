__all__ = ("db", )
from typing import TYPE_CHECKING, Type

from flask_sqlalchemy import BaseQuery
from flask_sqlalchemy import SQLAlchemy as SQLAlchemyGeneric, Model
from sqlalchemy.orm import Session
from sqlalchemy.orm import declared_attr

from sqlalchemy import Column, Integer


class Base(Model):
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)

    if TYPE_CHECKING:
        query: "BaseQuery"


class SQLAlchemy(SQLAlchemyGeneric):
    if TYPE_CHECKING:
        Model: Type[Base]
        session: Session


db = SQLAlchemy(model_class=Base)
