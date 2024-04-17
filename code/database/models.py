from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .db_setup import Base

class User(Base):
    """
    Database model for the users table.

    Attributes:
        id (int): Primary key for the user.
        username (str): User's username.
        email (str): User's email address (should be unique).
    """
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(15), nullable=False)
    lastname = Column(String(15), nullable=True)
    email = Column(String(50), unique=True, nullable=False)

