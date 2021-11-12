from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class ShowUser(BaseModel):
    username: str
    password: str
    class Config():
        orm_mode = True

class User_Request(BaseModel):
    image_url: str
    time: str

class ShowUser_Request(BaseModel):
    image_url: str
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    usernames: Optional[str] = None