
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager



def scrape():
    #setup splinter

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    listings = {}


    # Scrape title and teaser into Soup
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    
    html = browser.html
    soup = bs(html, "html.parser")

    listings["title"] = soup.find('div', class_='content_title').get_text()
    listings["article_teaser"] = soup.find('div', class_='article_teaser_body').get_text()

    
    # Scrape page into Soup
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')
    image_source = soup.find('img', class_='headerimage fade-in')['src']

    listings["featured_image_url"] = url + image_source


    # Scrape table
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    tables = pd.read_html(url)
    mars_earth_compare = tables[0]
    listings["table"] = mars_earth_compare.to_html()

    
    
    browser.quit()

    return listings


