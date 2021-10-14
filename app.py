from flask.json import jsonify
from selenium import webdriver
from flask import Flaskm, jsonify
import asyncio
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
    driver.quit()
    return pesquisa

@app.route('/')
def index():
    return 'Ok!'

@app.route('/teste')
async def teste():
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(realizar_teste(abrir_navegador()))
    return jsonify({"retorno":result})

if __name__ == '__main__':
    app.run()