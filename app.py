import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=cms-server-12345.database.windows.net;"
    "DATABASE=cms;"
    "UID=cmsadmin;"
    "PWD=CMS4dmin;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

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
