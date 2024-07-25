from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Primeiro Wait apos examinar codigo web zap
xpath1 = "/html/body/div[1]/div/div/div[2]/div[3]/header/header/div/div/h1" 

# Segundo Wait para dar Enter e enviar mensagem
xpath = "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p" 

def abrir_chrome():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    esperar_login()
    return driver

def esperar_login(driver):
    wait = WebDriverWait(driver, timeout=120)
    elemento = wait.until(lambda driver: driver.find_element(By.XPATH, xpath1))

# numero = "459999999"
# mensagem = "Olá, estou enviando esta mensagem via Selenium!"
 
def mandar_mensagem(driver, nome, numero, divida):
    mensagem = f"{nome} sua nova divida é {divida}"
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
 
    driver.get(link)

    wait = WebDriverWait(driver, timeout=120)

# Espera até que o elemento seja visível na página
    elemento = wait.until(lambda driver: driver.find_element(By.XPATH, xpath))
    driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)

def fechar_navegador(driver):
    input("Fechar Navegador")
    driver.quit()

if __name__ == '__main__':
    pass