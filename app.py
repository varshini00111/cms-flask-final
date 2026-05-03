from flask import Flask, render_template, request
import pyodbc
from azure.storage.blob import BlobServiceClient
import os
import uuid

app = Flask(__name__)

# DATABASE CONNECTION (SECURE)
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={os.environ.get('DB_SERVER')};"
    f"DATABASE={os.environ.get('DB_NAME')};"
    f"UID={os.environ.get('DB_USER')};"
    f"PWD={os.environ.get('DB_PASSWORD')};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

# BLOB STORAGE (SECURE)
blob_connection_string = os.environ.get("BLOB_CONNECTION")
container_name = "images"
storage_account_name = os.environ.get("STORAGE_NAME")

@app.route('/')
def home():
    return "CMS is running on Azure!"

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            title = request.form['title']
            author = request.form['author']
            body = request.form['body']

            image = request.files['image']

            image_url = None

            if image and image.filename != "":
                filename = str(uuid.uuid4()) + "_" + image.filename

                blob_service_client = BlobServiceClient.from_connection_string(blob_connection_string)
                blob_client = blob_service_client.get_blob_client(
                    container=container_name,
                    blob=filename
                )

                blob_client.upload_blob(image, overwrite=True)

                image_url = f"https://{storage_account_name}.blob.core.windows.net/{container_name}/{filename}"

            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO articles (title, author, body, image_url) VALUES (?, ?, ?, ?)",
                (title, author, body, image_url)
            )

            conn.commit()
            conn.close()

            return "✅ Article Saved!"

        except Exception as e:
            return f"❌ ERROR: {str(e)}"

    return render_template("create.html")
