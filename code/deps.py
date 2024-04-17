from code.database.db_setup import SessionLocal
from .api import GmailApi

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_gmail_api():

    return GmailApi()