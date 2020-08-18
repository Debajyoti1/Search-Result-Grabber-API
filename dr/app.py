from selenium import webdriver
from bs4 import BeautifulSoup

driver=webdriver.Chrome()
text='gadgetguys'
driver.get('https://google.co.in/search?q='+text)
a=driver.page_source
driver.close()
with open('my.txt', "w", encoding="utf-8") as f:
    f.write(a)


