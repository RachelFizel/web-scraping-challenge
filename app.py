#################################################
# import Flask and needed things
#################################################
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
# # Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")

#################################################
# Flask Routes
#################################################
@app.route("/")
def index():
    # return(
    #      f"Available Routes:<br/>"
    #      f"/scrape<br/>"   
    # )
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)
    


@app.route("/scrape")
def scraper():
    #return(f'test')
    #scraped the page, adds the code to the database, and returns to the index route
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_info()
    
    mars.update({}, mars_data, upsert=True)
    #return(listings_data)
    return redirect("/", code=302)


#################################################
# Flask Closing Code
#################################################
if __name__ == "__main__":
    app.run(debug=True)
