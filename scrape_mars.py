#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo


def scrape_info():
    mars = {}



    #setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # # Scraping NASA Mars News - collect the News Title and  Pargraph Text


    url = 'https://redplanetscience.com/'
    browser.visit(url)



    html = browser.html
    soup = bs(html, 'html.parser')


    articles = soup.find('div', class_='list_text')

    #texts
    #for article in articles:
    title = articles.find('div', class_='content_title').text
    article_teaser = articles.find('div', class_='article_teaser_body')
        

    print("-----Title-----")
    print(title)
    print("-----Article Teaser-----")
    print(article_teaser.text)

    mars['news_title'] = title
    mars['article'] = article_teaser.text


    # # Scraping JPL Mars Space Images - collect the url for the Mars Image

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)



    html = browser.html
    soup = bs(html, 'html.parser')
    image_source = soup.find('img', class_='headerimage fade-in')['src']

    print(image_source)



    featured_image_url = url + image_source
    featured_image_url 

    mars['featured_image'] = featured_image_url


    # # Scraping Mars Facts - collect the table containing facts about planet


    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)


    tables = pd.read_html(url)
    tables


    mars_earth_comparicon_df = tables[0]
    mars_earth_comparicon_df.head(10)



    mars_earth_comparicon_df = tables[0]
    mars_earth_comparicon_df.columns = ["description", "Mars", "Earth"]
    mars_earth_comparicon_df.set_index('description', inplace=True)
    mars_earth_comparicon_df.head(10)




    html_table = mars_earth_comparicon_df.to_html()
    html_table



    mars['facts'] = html_table


    # # Scraping Mars Hemispheres - collect images for each hemisheres


    url = 'https://marshemispheres.com/'
    browser.visit(url)



    #for x in range(1, 4):
    hemisphers_image_url = []

    html = browser.html
    soup = bs(html, 'html.parser')

    #images = soup.find_all('div', class_='description')
    #images = soup.find_all('div', class_='itemLink product-item')

    images = browser.find_by_css("a.product-item img")

    for image in range(len(images)):
    # #for x in range(1, 4):
        hemisphers = {}
        
        browser.find_by_css("a.product-item img")[image].click()
        
        element = browser.links.find_by_text('Sample').first
        
        hemisphers['img_url'] = element['href']
        
        hemisphers['title'] = browser.find_by_css('h2.title').text
        
        hemisphers_image_url.append(hemisphers)
        
        browser.back()
        

    #     #browser.links.find_by_partial_text('next').click()


    print('--------------------------------------')
    print (hemisphers_image_url)

    mars['hemisphers'] = hemisphers_image_url



    browser.quit()

    return mars


