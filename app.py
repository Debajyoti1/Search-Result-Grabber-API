from flask import Flask, render_template, url_for, request, session, redirect, g
from selenium import webdriver
import os
import threading
from fake_useragent import UserAgent
import time
ua = UserAgent()
usrand=ua.random
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

app = Flask(__name__)
app.secret_key='Hellothere'

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/google',methods=['GET','POST'])
def google():
    se='Google'
    return 'hi'
if __name__ == '__main__':
    app.run(debug=True)