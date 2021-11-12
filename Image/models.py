from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .database import Base
from sqlalchemy.orm import relationship
import datetime

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
    time = Column(DateTime,default=datetime.datetime.utcnow())
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship("User", back_populates="creator")