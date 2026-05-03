from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ CMS is running on Azure!"

@app.route('/login')
def login():
    return "Login Page"

@app.route('/create')
def create():
    return "Create Article Page"

# Azure needs this
if __name__ == "__main__":
    app.run()
