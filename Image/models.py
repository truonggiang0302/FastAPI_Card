from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from .database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    creator = relationship("User_Request", back_populates="users")


class User_Request(Base):
    __tablename__= "user_request"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    time = Column(TIMESTAMP)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship("User", back_populates="creator")