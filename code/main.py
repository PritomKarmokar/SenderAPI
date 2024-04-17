from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session

from .database import models, schemas
from .database.db_setup import engine
from .deps import get_db, get_gmail_api
from .api import GmailApi
from .crud import *
# Create the database tables
models.Base.metadata.create_all(bind=engine)

description = """
SenderApi helps you to send Email notification when a new user registers. 🚀

## Users

You will be able to:
* **Register users**
"""

app = FastAPI(
    title="SenderApi",
    description=description
)


@app.get("/")
def root():
    return {
        "msg": "Welcome to the SenderApi"
    }


@app.post("/register/", response_model=schemas.User)
def register_user(user: schemas.UserCreate,  background_tasks: BackgroundTasks, db: Session = Depends(get_db), service: GmailApi = Depends(get_gmail_api)):
    """
    Endpoint to register a new user.

    Args:
        user (schemas.UserCreate): User creation data received from the client.
        background_tasks (BackgroundTasks): BackgroundTasks instance to execute tasks asynchronously.
        db (Session): Database session object.
        service (GmailApi): Instance of the GmailApi service used for sending email notifications.

    Returns:
        schemas.User: The created user object.
    """

    existing_user = get_user_by_email(db, user.email)
    
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system"
        )
    
    new_user = create_user(db, user=user)

    background_tasks.add_task(
        send_notification,
        service,
        new_user.email
    )

    return new_user