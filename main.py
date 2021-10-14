from selenium import webdriver
from flask import Flask
import os

app = Flask(__name__)

def abrir_navegador():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    return driver

def realizar_teste(driver):
    driver.get('https://www.google.com')
    pesquisa = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[1]/a[4]').text
    print(pesquisa)
    driver.quit()

@app.route('/')
def index():
    return 'Ok!'

@app.route('/teste')
def teste():
    return 'Tentativa'

if __name__ == '__main__':
    app.run()