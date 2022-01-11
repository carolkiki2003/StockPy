#爬熱門文章一篇
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

my_options = Options() 
my_options.add_argument("--headless")
my_options.add_argument("--start-maximized") 
my_options.add_argument("--incognito")
path = "./chromedriver"
driver = webdriver.Chrome(path, options = my_options)

# get content
cookies = {"platform": "pc"}
driver.get("https://www.cmoney.tw/forum/popular/buzz")
x = driver.find_element(By.XPATH, "//div[@class = 'announcement__close']")
x.click()
sp = driver.find_elements(By.XPATH, "//article[@class = 'articleContent']")
txt = sp[0].find_element(By.XPATH, "//div[@class = 'textRule__text text-white-800']")
b = txt.find_element(By.XPATH, ".//span").text 

    
# get first name and stock list
re = requests.get("https://www.cmoney.tw/forum/popular/buzz", cookies = cookies)
soup = BeautifulSoup(re.text, "html.parser")
tag = soup.find_all("div", {"class" : "articleTags"})
stock = tag[0].find_all("div", {"class":'articleTags__text text-white-800'})
name = soup.find("div", {"class":"member__name text-white-800"})

print(name.text.strip())
print(" ".join([i.text.strip() for i in stock]))
print(b)