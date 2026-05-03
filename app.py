from flask import Flask, render_template, request
import pyodbc
from azure.storage.blob import BlobServiceClient
import os
import uuid

app = Flask(__name__)

# =========================
# ✅ DATABASE CONNECTION
# =========================
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={os.environ.get('SQL_SERVER')};"
    f"DATABASE={os.environ.get('SQL_DATABASE')};"
    f"UID={os.environ.get('SQL_USER_NAME')};"
    f"PWD={os.environ.get('SQL_PASSWORD')};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

# =========================
# ✅ BLOB STORAGE
# =========================
blob_connection_string = os.environ.get("BLOB_CONNECTION_STRING")
container_name = os.environ.get("BLOB_CONTAINER")
storage_account_name = os.environ.get("BLOB_ACCOUNT")

# =========================
# 🔍 DEBUG CHECK (VERY IMPORTANT)
# =========================
if not blob_connection_string:
    print("❌ ERROR: Missing BLOB_CONNECTION_STRING")

if not os.environ.get("SQL_SERVER"):
    print("❌ ERROR: Missing SQL ENV VARIABLES")

# =========================
# HOME ROUTE
# =========================
@app.route('/')
def home():
    return "CMS is running on Azure!"

# =========================
# CREATE ARTICLE
# =========================
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            title = request.form['title']
            author = request.form['author']
            body = request.form['body']

            # ✅ SAFE IMAGE FETCH
            image = request.files.get('image')
            image_url = None

            # =========================
            # 📸 IMAGE UPLOAD TO BLOB
            # =========================
            if image and image.filename:
                filename = str(uuid.uuid4()) + "_" + image.filename

                blob_service_client = BlobServiceClient.from_connection_string(blob_connection_string)
                blob_client = blob_service_client.get_blob_client(
                    container=container_name,
                    blob=filename
                )

                blob_client.upload_blob(image, overwrite=True)

                image_url = f"https://{storage_account_name}.blob.core.windows.net/{container_name}/{filename}"

            # =========================
            # 💾 SAVE TO DATABASE
            # =========================
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
