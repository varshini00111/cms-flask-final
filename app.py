from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "CMS is running on Azure!"

# Create article page
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        body = request.form.get('body')

        return f"Article Created: {title} by {author}"

    return render_template("create.html")

if __name__ == '__main__':
    app.run()
