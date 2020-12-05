<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Web Scraping - Mission to Mars</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/bimalkprabha/python-api-challenge//issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/bimalkprabha/python-api-challenge//pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">A Responsive Web Visualization Dashboard using Flask framework to create a application that scrapes various websites for data related to the Mars and displays the information in a single HTML page.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Hosting](#trends)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
In building this dashboard based on two parts. First part consist of scraping the data from using jupyter noebook and designing a dashboard using templated in Flask Framework.

## 🏁 Getting Started <a name = "getting_started"></a>

## Step 1 - Scraping

Completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Created a Jupyter Notebook file called `mission_to_mars.ipynb` and used this to complete all of the scraping and analysis tasks. 

### NASA Mars News

* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text. Assigned the text to variables that  can be referenced later.

```python
# Code:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* Visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`.

* Made sure to find the image url to the full size `.jpg` image.

* Made sure to save a complete url string for this image.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Facts

* Visited the Mars Facts webpage [here](https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Used splinter to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -


## Tasks

* Used Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Used Pymongo for CRUD applications for your database. 

* Used Bootstrap to structure my HTML template.


## ✍️ Hosting <a name = "trends"></a></br>

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Started by converting my Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of my scraping code from above and returned one Python dictionary containing all of the scraped data.

* Next, created a route called `/scrape` that will import your `scrape_mars.py` script and called my `scrape` function.

  * Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that will query your Mongo database and passed the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that will take the mars data dictionary and displayed all of the data in the appropriate HTML elements. 
![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)

- - -



## 🎉 Acknowledgements <a name = "acknowledgement"></a>
- UWA Data Science</br>


