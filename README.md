# SenderAPI
Developing a RESTAPI using FastAPI that will send an email when someone registers themselves

## Installation

### Clone the repository

```bash
git clone git@github.com:PritomKarmokar/SenderAPI.git
cd SenderAPI
```

### Run Locally with venv
Ensure you have Python and pip installed on your machine.

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On Unix or macOS:
        ```bash
        source venv/bin/activate
        ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the FastAPI app:
    ```bash
    uvicorn code.main:app --reload
    ```

### Run with Docker using docker-compose

Ensure you have Docker and docker-compose installed on your machine.

1. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

## Usage

Access the app at [http://localhost:8000](http://localhost:8000)

## API Documentation

Access API documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)



## Configuration

### Gamil API Client Secret 

01. [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)

02. [Enable the API](https://developers.google.com/gmail/api/quickstart/python#enable_the_api)

03. [Configure the OAuth consent screen](https://developers.google.com/gmail/api/quickstart/python#configure_the_oauth_consent_screen)

04. [Authorize credentials for a desktop application](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application)

05. Finally store the 'credentials.json' in `code/api_credentials` directory

### Sending Email Notification

When a user registers through the API, a welcome email will be sent using the Gmail API. The endpoint for registration is:

- **POST /register**: This endpoint takes the user's firstname,
lastname (optional) and email address and saves it to the database, then sends a welcome email using Gmail API.
