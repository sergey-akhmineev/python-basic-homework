"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Boolean,
    create_engine,
    ForeignKey,
    Text
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, declared_attr, InstrumentedAttribute

engine = create_async_engine("postgresql+asyncpg://postgres:secretpassword@localhost:5432/postgres", echo=True)

Base = declarative_base(bind=engine)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
Session = async_session


class User(Base):
    __tablename__ = "users"

    def __init__(self, id: int, name: str, username: str, email: str):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, default="", server_default="")
    username = Column(String(32), nullable=False, default="", server_default="")
    email = Column(String(128), nullable=False, default="", server_default="")
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    def __init__(self, id: int, title: str, user_id: int, body: str):
        self.id = id
        self.title = title
        self.user_id = user_id
        self.body = body

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False, default="", server_default="")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    body = Column(String(256), nullable=False, default="", server_default="")
    user = relationship(User, back_populates="posts")
