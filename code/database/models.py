from sqlalchemy import Column, Integer, String
from .db_setup import Base

class User(Base):
    """
    Database model for the users table.

    Attributes:
        id (int): Primary key for the user.
        firstname (str): User's firstname.
        lastname (str): User's lastname
        email (str): User's email address (should be unique).
    """
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(15), nullable=False)
    lastname = Column(String(15), nullable=True)
    email = Column(String(50), unique=True, nullable=False)

