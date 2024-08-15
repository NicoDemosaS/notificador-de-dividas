from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import os

# XPaths para os elementos
xpath1 = "/html/body/div[1]/div/div/div[2]/div[3]/header/header/div/div/h1" 
xpath = "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p" 

def abrir_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=C:/Users/bar/AppData/Local/Google/Chrome/User Data")  # Ajuste conforme necessário
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://web.whatsapp.com/")
    return driver

def esperar_login(driver):
    wait = WebDriverWait(driver, timeout=120)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath1)))

def mandar_mensagem(driver, numero, mensagem):
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    driver.get(link)
    wait = WebDriverWait(driver, timeout=120)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)

if __name__ == '__main__':
    driv = abrir_chrome()
    
    nome = 'Nicolas'
    numero = '45999232707'
    divida = 500
    
    while True:
        op = input('OPÇÃO (1-salvar, 2-carregar, 3-atualizar, 4-enviar mensagem, 5-fechar): ')
        if op == '4':
            mensagem = f'{nome} sua divida é de R${divida}'
            mandar_mensagem(driv, numero, mensagem)
        elif op == '5':
            driv.quit()
            break
