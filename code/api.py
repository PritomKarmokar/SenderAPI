import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage

# Constants
# BASE_DIR = r"/code/api_credentials"
BASE_DIR = "code/api_credentials"
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")
TOKEN_PATH = os.path.join(BASE_DIR, "token.json")

SCOPES = ['https://mail.google.com/']
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']


class GmailApi:
    def __init__(self):
        # Initialize the GmailService with credentials
        self.creds = self.get_credentials()

    def get_credentials(self):
        """
        Retrieves stored credentials or initiates OAuth2 flow to get new credentials from the Gmail Api
        """
        creds = None

        if os.path.exists(TOKEN_PATH):
            creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_PATH, SCOPES
                )
                creds = flow.run_local_server(port=0)

            with open(TOKEN_PATH, "w") as token:
                token.write(creds.to_json())

        return creds
    
    
    def send_email(self, to, subject, body):
        """
        Create and send an email using Gmail API
        Args:
            to (str): Email address of the recipient
            subject (str): Subject of the email
            body (str): Body content of the email
        Returns:
            dict: Response containing message id if successful, None otherwise
        """
        try:
            # Build Gmail service
            service = build("gmail", "v1", credentials=self.creds)
            results = service.users().labels().list(userId="me").execute()
            labels = results.get("labels", [])

            if not labels:
                print("No labels found.")
            else:
                print("Labels: ")
                for label in labels:
                    print(label["name"])

            # Create email message
            message = EmailMessage()
            message.set_content(body)
            message["To"] = to
            message["Subject"] = subject
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            raw_message = {"raw": encoded_message}

            # Send email
            send_message = (
                service.users()
                .messages()
                .send(userId="me", body=raw_message)
                .execute()
            )
            print(f'Message Id: {send_message["id"]}')
            return send_message

        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

