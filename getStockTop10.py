#爬top10
import re
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def PopularStocker():
    my_options = Options() 
    my_options.add_argument("--headless")
    my_options.add_argument("--start-maximized") 
    my_options.add_argument("--incognito")
    path = "./chromedriver"
    driver = webdriver.Chrome(path, options = my_options)


    url = requests.get("https://www.cmoney.tw/forum/popular/stock")
    soup = BeautifulSoup(url.text, "html.parser")
    tops = soup.find_all("h3", {"class": 'headline__title'})
    top_n = []
    stocks =[]
    for i in range(0,10):
        top_stock = tops[i].text.strip()
        num = re.sub("[^0-9]", "", top_stock)
        top_n.append(num)
        stocks.append(top_stock)
    return stocks