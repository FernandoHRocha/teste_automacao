from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, jsonify
import os
import asyncio

app = Flask(__name__)

async def abrir_navegador():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver = webdriver.Chrome(executable_path=("chromedriver.exe"), options=chrome_options)
    driver.get('https://www.comprasnet.gov.br/seguro/loginportal.asp')
    wait = WebDriverWait(driver,100)
    pesquisa = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/main/div/div/div[2]/main/h3'))).text
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