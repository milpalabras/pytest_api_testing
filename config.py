import os
from dotenv import load_dotenv

load_dotenv(verbose=True, override=True)
BASE_URI = os.getenv("BASE_URI")
SESSION_CONFIRMATION_ENDPOINT = os.getenv("SESSION_CONFIRMATION_ENDPOINT")
LOGIN_ENDPOINT = "actors/cProfileActor/login?"
LOGIN = os.getenv("LOGIN")
LOGIN2 = os.getenv("LOGIN2")
PASSWORD2 = os.getenv("PASSWORD2")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_EMAIL2 = os.getenv("LOGIN_EMAIL2")
LOGIN_DNI = os.getenv("LOGIN_DNI")
PASSWORD = os.getenv("PASSWORD")
PARAMS = os.getenv("PARAMS")
SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
PROTOCOL = os.getenv("PROTOCOL")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_PORT = os.getenv("SQL_PORT")

ORACLE_SERVER = os.getenv("ORACLE_SERVER")
ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
ORACLE_DATABASE = os.getenv("ORACLE_DATABASE")
ORACLE_PORT = os.getenv("ORACLE_PORT")
SERVICE_NAME = os.getenv("SERVICE_NAME")

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
GMAI_IMAP_SERVER = os.getenv("IMAP_SERVER")
