from pydantic import BaseModel, Field, EmailStr, ConfigDict

class UserBase(BaseModel):
    """
    Base schema for a user.

    Attributes:
        firstname (str): First name of the user.
        lastname (str): Last name of the user.
        email (EmailStr): Email address of the user.
    """

    firstname: str = Field(min_length= 3, 
                          max_length=15)
    
    lastname: str = Field(min_length=3,
                          max_length=50)
    
    email: EmailStr = Field(max_length=50)

class UserCreate(UserBase):
    """
        Schema for user creation, inherits from UserBase.
    """
    model_config = ConfigDict(extra='forbid') # Forbid any extra attributes

class User(UserBase):
    """
    Schema for default user model representation, inherits from UserBase.

    Attributes:
        id (int): User's identifier.
    """
    
    id : int

    