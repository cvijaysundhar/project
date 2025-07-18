from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀  Hello from your Flask app on GCP!"

@app.route('/about')
def about():
    return "This is a simple web app for practicing Git & GCP!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)

