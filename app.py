from flask import Flask, render_template, request, redirect, url_for
import pyodbc
from azure.storage.blob import BlobServiceClient
import os
import uuid
import logging

app = Flask(__name__)

# =========================
# LOGGING (VERY IMPORTANT)
# =========================
logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

# =========================
# DATABASE CONNECTION
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
# BLOB STORAGE
# =========================
blob_connection_string = os.environ.get("BLOB_CONNECTION_STRING")
container_name = os.environ.get("BLOB_CONTAINER")
storage_account_name = os.environ.get("BLOB_ACCOUNT")

# =========================
# HOME ROUTE
# =========================
@app.route('/')
def home():
    return '''
    <h1>CMS Running on Azure 🚀</h1>
    <a href="/login">Login</a><br>
    <a href="/create">Create Article</a>
    '''

# =========================
# LOGIN ROUTE
# =========================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # HARD-CODED USER
        if username == "admin" and password == "pass":
            app.logger.info("admin logged in successfully")
            return redirect(url_for('home'))
        else:
            app.logger.error("Invalid login attempt")
            return "❌ Invalid username or password"

    return '''
        <h2>Login</h2>
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit">
        </form>
    '''

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

            image = request.files.get('image')
            image_url = None

            # IMAGE UPLOAD
            if image and image.filename:
                filename = str(uuid.uuid4()) + "_" + image.filename

                blob_service_client = BlobServiceClient.from_connection_string(blob_connection_string)
                blob_client = blob_service_client.get_blob_client(
                    container=container_name,
                    blob=filename
                )

                blob_client.upload_blob(image, overwrite=True)

                image_url = f"https://{storage_account_name}.blob.core.windows.net/{container_name}/{filename}"

            # DATABASE SAVE
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO articles (title, author, body, image_url) VALUES (?, ?, ?, ?)",
                (title, author, body, image_url)
            )

            conn.commit()
            conn.close()

            return "✅ Article Saved Successfully!"

        except Exception as e:
            return f"❌ ERROR: {str(e)}"

    return render_template("create.html")

# =========================
# RUN APP
# =========================
if __name__ == '__main__':
    app.run()
