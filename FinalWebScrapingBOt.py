# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:10:11 2020

@author: admin
"""
from selenium import webdriver
import os
os.chdir("D:\\ketsaal data\\scraping\\Products Scrapped")
import requests
from fake_useragent import UserAgent
import pandas as pd
import bs4

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
specifications = []


driver = webdriver.Chrome("C:\\Users\\admin\\AppData\\local\\Temp\\Rar$EXa12492.22315\\chromedriver")
## initializing the UserAgent object
user_agent = UserAgent()
#a = "spider shaker"
a = input("Product Name- ")
for i in range(1,10):
    url = "https://www.flipkart.com/search?q={0}&page={1}"
#url = "https://www.amazon.in/s?k={0}"

    url = url.format(a,i)
    driver.get(url)
    
     ## getting the reponse from the page using get method of requests module
    page = requests.get(url, headers={"user-agent": user_agent.chrome})

    ## storing the content of the page in a variable
    html = page.content

    ## creating BeautifulSoup object
    page_soup = bs4.BeautifulSoup(html, "html.parser")
    
    for containers in page_soup.findAll('div',{'class':'_3liAhj'}):
#        name=containers.div.img['alt']
        name=containers.find('a', attrs={'class':'_2cLu-l'})
        price=containers.find('div', attrs={'class':'_1vC4OE'})
        rating=containers.find('div', attrs={'class':'hGSR34'})
        specification = containers.find('div', attrs={'class':'_1rcHFq'})
        products.append(name.text)
        prices.append(price.text)
        specifications.append(specification.text) if type(specification) == bs4.element.Tag  else specifications.append('NaN')
        ratings.append(rating.text) if type(rating) == bs4.element.Tag  else ratings.append('NaN')
    df = pd.DataFrame({'Product Name':products,'Price':prices, 'specification':specifications, 'Rating':ratings})
    
df.to_excel('Name.xlsx', index=False, encoding='utf-8')