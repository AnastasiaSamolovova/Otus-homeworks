__all__ = ("Post", )

from sqlalchemy import Column, String, Text
from .database import db


class Post(db.Model):
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, nullable=False, default='N/A')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r})"
