from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")




@app.route("/")
def index():
    mars = mongo.db.mars_db.find_one()
    return render_template("index.html",mars=mars, planet = "Mars")

@app.route("/scrape")
def scraper():
     mars = mongo.db.mars
     mars_data = scrape_mars.scrape_news()
    #  mars_col = scrape_mars.feature_img()
    #  mars_col = scrape_mars.mars_facts()
    #  mars_col = scrape_mars.mars_hem()
    #  mars_col = scrape_mars.scrape_news()
     mars.update({}, mars_data, upsert=True)
     return redirect("/", code=302)
if __name__ == "__main__":
    app.run(debug=True)