from selenium import webdriver
from flask import Flask, jsonify
import os
import asyncio

app = Flask(__name__)

async def abrir_navegador():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.get('https://www.google.com')
    pesquisa = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[1]/a[4]').text
    driver.quit()
    return pesquisa

@app.route('/')
def index():
    return 'Ok!'

@app.route('/teste')
def teste():
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(abrir_navegador())
    return jsonify({"retorno":result})

if __name__ == '__main__':
    app.run()