import pyodbc

conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_server.database.windows.net;DATABASE=your_db;UID=your_user;PWD=your_password"

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
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

    return render_template("create.html")
