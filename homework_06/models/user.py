__all__ = ("User", )

from sqlalchemy import Column, String
from .database import db


class User(db.Model):
    name = Column(String(100), unique=False, nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"email={self.email})")
