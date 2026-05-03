from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ CMS is running on Azure!"

if __name__ == "__main__":
    app.run()
