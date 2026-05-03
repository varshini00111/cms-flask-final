import pyodbc

import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=cms-server-12345.database.windows.net;"
    "DATABASE=cms;"
    "UID=cmsadmin;"
    "PWD=CMS4dmin;"
)
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

return redirect('/')
    return render_template("create.html")
