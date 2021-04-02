
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

    browser.quit()


    # # Scrape page into Soup
    # url = 'https://spaceimages-mars.com/'
    # browser.visit(url)

    # html = browser.html
    # soup = bs(html, 'html.parser')
    # image_source = soup.find('img', class_='headerimage fade-in')['src']

    # listings["featured_image_url"] = url + image_source
    

    return listings


