from flask import Flask, render_template, request
import pyodbc
from azure.storage.blob import BlobServiceClient
import os
import uuid

app = Flask(__name__)

# ✅ DATABASE CONNECTION (FIXED NAMES)
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={os.environ.get('SQL_SERVER')};"
    f"DATABASE={os.environ.get('SQL_DATABASE')};"
    f"UID={os.environ.get('SQL_USER_NAME')};"
    f"PWD={os.environ.get('SQL_PASSWORD')};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

# ✅ BLOB STORAGE (FIXED NAMES)
blob_connection_string = os.environ.get("BLOB_CONNECTION_STRING")
container_name = os.environ.get("BLOB_CONTAINER")
storage_account_name = os.environ.get("BLOB_ACCOUNT")
