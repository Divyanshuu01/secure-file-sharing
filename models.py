# models.py

from sqlalchemy import Column, Integer, String
from database import Base
# models.py (add this to your existing models)
from pydantic import BaseModel

class SignupRequest(BaseModel):
    username: str
    password: str


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)  # Store hashed passwords
    user_type = Column(String)  # "admin" or "client"
