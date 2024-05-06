from sqlalchemy.orm import Session
from fastapi import BackgroundTasks
from pydantic import EmailStr
from .database import models, schemas
from .api import GmailApi

def create_user(db: Session, user: schemas.UserCreate):
    """
    Create a new user in the database.

    Args:
        db (Session): Database session object.
        user (schemas.UserCreate): User creation data.

    Returns:
        models.User: The created user object.
    """
    new_user = models.User(firstname=user.firstname, lastname=user.lastname, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_email(db: Session, emailAddress: EmailStr):
    """
    Retrieves a user from the database based on their email address.

    Args:
        db (Session): The database session object.
        emailAddress (EmailStr): The email address of the user to retrieve.

    Returns:
        models.User: The user object corresponding to the provided email address, or None if not found.
    """

    return db.query(models.User).filter(models.User.email == emailAddress).first()



async def send_notification(service: GmailApi, emailAddress: EmailStr):
    """
    Asynchronously sends a welcome notification email to the specified email address.

    Args:
        service (GmailApi): An instance of the GmailApi service used to send emails.
        emailAddress (EmailStr): The email address to which the notification will be sent.

    Returns:
        None
    """
     
    subject = "Welcome to the App !"
    body = "Registration process is completed"
    
    try:
        service.send_email(emailAddress, subject=subject, body=body)
        print("Email sent successfully")
    except Exception as error:
        print(f"Error : {error}")