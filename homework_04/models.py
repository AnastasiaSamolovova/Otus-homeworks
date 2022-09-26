"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

from sqlalchemy import Column, String, ForeignKey, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from base import Base
import os

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd!@localhost:5432/blog"

async_engine: AsyncEngine = create_async_engine(
    PG_CONN_URI,
    echo = False,
)

async_session = sessionmaker(
    async_engine,
    class_ = AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base(cls=Base)
Session = async_session()     


class User(Base):
    name = Column(String(100), unique = False, nullable = False)
    username = Column(String(100), nullable = False)
    email = Column(String(100), nullable = False)
    
    posts = relationship("Post", back_populates="user", uselist=True)
    
    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"email={self.email})"
        )
    
class Post(Base):
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, nullable=False, default = 'N/A')
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates = 'posts')
    
    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, user_id={self.user_id})"

    
async def create_tables():
    async with async_engine.begin() as conn:
        print("todo: drop all")
        await conn.run_sync(Base.metadata.drop_all)
        print("todo: create all")
        await conn.run_sync(Base.metadata.create_all)
        
        
async def create_users(session: AsyncSession, *users_data: list[dict]) -> list[User]:
    users = [
        User(id=user_data['id'], name=user_data['name'], username=user_data['username'], email=user_data['email'], posts=[])
        for user_data in users_data
    ]
    session.add_all(users)
    await session.commit()
    print("created users", users)

    return users

async def create_posts(session: AsyncSession, *posts_data: list[dict]) -> list[Post]:
    posts = [
        Post(id=post_data['id'], user_id=post_data['userId'], title=post_data['title'], body=post_data['body'])
        for post_data in posts_data
    ]
    session.add_all(posts)
    await session.commit()
    print("created posts", posts)

    return posts