import requests
from bs4 import BeautifulSoup as bs
import time
from splinter import Browser
import os
import pandas as pd
driver_path = os.environ.get("SPLINTER_PATH")

def init_browser():
    executable_path = {'executable_path':r"C:\bin\chromedriver.exe"}
    browser = Browser('chrome', **executable_path)
    return browser
    
def scrape_news():
    # browser = init_browser()
    mars_info = {}
    url ="https://mars.nasa.gov/news/"
    data = requests.get(url)
    soup = bs(data.text,'html.parser')
    data = soup.find_all('div',class_='slide')
    for news in data:
        mars_info['title'] = news.find('div','content_title').text
        mars_info['paragraph'] = news.find('div','rollover_description_inner').text
        
        # print(title,paragraph)
    return(mars_info)
def feature_img():
    browser = init_browser()
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    browser.find_by_id('full_image').click()
    browser.is_element_present_by_text("more info", wait_time=1)
    more_info_element = browser.links.find_by_partial_text("more info")
    more_info_element.click()
    img_url = browser.url
    html_img = requests.get(img_url)
    soup_img = bs(html_img.text,'html.parser')
    main_img = soup_img.find('img',class_="main_image")['src']
    main_img_url = "https://www.jpl.nasa.gov" + main_img
    # print(main_img_url)
    browser.visit(f'{main_img_url}')
    time.sleep(2)
    browser.quit()
    return main_img_url

def mars_facts():
    facts_url = "https://space-facts.com/mars/"
    facts = pd.read_html(facts_url)

    df = facts[0]   
    df.rename(columns={
    0:'Description',
    1:'Mars'
},inplace=True) 
    table_html = df.to_html(index =False,justify ='center')
    # table_html.replace('/n','')
    # print(table_html)
    return table_html
    
def mars_hem():
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_data = requests.get(hemisphere_url)
    hemisphere_data = bs(hemisphere_data.text,'html.parser')
    hemisphere_data = hemisphere_data.find_all('div',class_ ="item")
    hemisphere_image_urls = []
    for links in hemisphere_data:

            end_link = links.a['href']
            image_link = "https://astrogeology.usgs.gov/" + end_link 
            browser = init_browser()
            browser.visit(image_link)
            html = browser.html
            time.sleep(2)
            soup= bs(html, "html.parser")
            downloads = soup.find("div", class_="downloads")
            image_url = downloads.find("a")["href"]

            a = {
            'title':links.h3.text,
            'img_url':image_url
                }
            hemisphere_image_urls.append(a)
            browser.quit()
    return hemisphere_image_urls
