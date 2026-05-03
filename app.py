from flask import Flask, render_template, request
import pyodbc

# CREATE FLASK APP (VERY IMPORTANT)
app = Flask(__name__)

# DATABASE CONNECTION STRING
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=cms-server-12345.database.windows.net;"
    "DATABASE=cms;"
    "UID=cmsadmin;"
    "PWD=CMS4dmin;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

# HOME ROUTE (REQUIRED)
@app.route('/')
def home():
    return "CMS is running on Azure!"

# CREATE ROUTE
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            title = request.form['title']
            author = request.form['author']
            body = request.form['body']

            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO articles (title, author, body) VALUES (?, ?, ?)",
                (title, author, body)
            )

            conn.commit()
            conn.close()

            return "✅ Article Saved!"

        except Exception as e:
            return f"❌ ERROR: {str(e)}"

    return render_template("create.html")
