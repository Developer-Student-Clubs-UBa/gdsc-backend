from sqlalchemy import Column, Integer, String
from database import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))

    def __str__(self):
        return f'Item(id={self.id}, task={self.task})'


class User(Base):
    __tablename__ = 'users'
    name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=True)
    password = Column(String(256), nullable=False)
    username = Column(String(256), nullable=False)
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    avatar_link = Column(String(256), nullable=True)
    bio = Column(String(256), nullable=True)

    def __str__(self):
        return self.username
