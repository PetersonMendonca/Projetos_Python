'''
Modelo de teste de multiplas mensagens com selenium Novo
'''

# Bibliotecas
from pathlib import Path
from time import sleep
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

# Caminhos de acesso aos arquivos
PATH_FILE = Path(__file__).parent
PATH_CHROMEDRIVE = PATH_FILE / 'chromedriver' /'chromedriver.exe'
PATH_DIR_GOOGLE = r'C:\Users\petri\AppData\Local\Google\Chrome\User Data\Perfil'
PATH_DIR_ROTEIROS = PATH_FILE / 'roteiros' / 'roteiro_shrek2.txt'

# Estruturação Browser Selenium
def chrome_browser(*options: str):
    
    chrome_options = webdriver.ChromeOptions()
    
    if options is not None:
        chrome_options.add_argument("user-data-dir=" + PATH_DIR_GOOGLE)
    
    chrome_services = Service(executable_path = PATH_CHROMEDRIVE)
    
    browser = webdriver.Chrome(service = chrome_services, options = chrome_options)
    
    return browser

def acessa_pagina(url):
    browser.get(url)
    sleep(15)

def modo_enche_o_saco():
    lista_pessoas = ['Gabi-chan']
    
    for nomes in lista_pessoas:
        # seleciona a pessoa
        input_element = browser.find_element(By.CSS_SELECTOR, '#side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text')
        input_element.send_keys(nomes)
        input_element.send_keys(Keys.ENTER)

        input_element2 = browser.find_element(By.CSS_SELECTOR, '#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text')
        while True:
            with open(PATH_DIR_ROTEIROS, 'r', encoding='utf-8') as roteiro:
                for frase in roteiro:
                    input_element2.send_keys(frase)
                    input_element2.send_keys(Keys.ENTER)

def seleciona_pessoa():
    click_element = browser.find_element(By.CSS_SELECTOR, '#pane-side > div > div > div > div:nth-child(8)')
    click_element.click()
    
def seleciona_multiplas_pessoas():
    lista_pessoas = ['Mãe', 'Pai', 'Mozão', 'Gabi-chan', 'Bruno TI - Pref']
    
    for nomes in lista_pessoas:
        input_element = browser.find_element(By.CSS_SELECTOR, '#side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text')
        input_element.send_keys(nomes)
        input_element.send_keys(Keys.ENTER)
        
        input_element2 = browser.find_element(By.CSS_SELECTOR, '#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text')
        input_element2.send_keys('Oi tudo bem?, isso é só um teste de mensagems para multiplas pessoas')
        input_element2.send_keys(Keys.ENTER)
        sleep(2)


# main do programa
if __name__ == '__main__':
    
    browser = chrome_browser('--disable-gpu', '--no-sandbox1')
    acessa_pagina('https://web.whatsapp.com/')
    
    #seleciona_pessoa()
    #seleciona_multiplas_pessoas()
    #modo_enche_o_saco() # modo de encher o saco com mensagens infinitas
    
    # input_element.send_keys('python')
    # input_element.send_keys(Keys.ENTER)
    
    sleep(223372036)
    browser.quit