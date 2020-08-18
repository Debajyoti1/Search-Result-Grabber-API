def Google(c,q):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from fake_useragent import UserAgent
    import os
    ua = UserAgent()
    usrand=ua.random
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("user-agent="+usrand)
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get('https://google.co.in/search?q='+q)
    source=driver.page_source
    driver.close()
    soup=BeautifulSoup(source)
    linktext=soup.findAll('div',class_='r')
    link=[]
    text=[]
    for i in linktext:
        link.append(i.a.get('href'))
        text.append(i.a.text)
    description=soup.findAll('span',class_='st')
    des=[]
    for j in description:
        des.append(j.text)
    ret=[]
    l=1
    for i,j,k in zip(link,text,des):
        ret.append(
        {l : {
            'link' : i,
            'text' : j,
            'description' : k
        }
        })
        l+=1
    return ret