from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)