import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib

mensagem = '''
Nome:\n
Divida:
'''
urllib.parse.quote(mensagem)

# Inicializa o navegador
navegador = webdriver.Firefox()
#navegador.get("https://web.whatsapp.com/")

input('CONFIRMAR: ')
xpath = "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span"

# Agora você pode enviar a mensagem
numero = 556791260268

link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
#navegador.get(link)
navegador.find_element_xpath(xpath).send_keys(Keys.ENTER)

