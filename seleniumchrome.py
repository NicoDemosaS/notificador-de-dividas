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
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=C:/Users/bar/AppData/Local/Google/Chrome/User Data")  # Ajuste conforme necessário
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://web.whatsapp.com/")
    return driver

def esperar_login(driver):
    wait = WebDriverWait(driver, timeout=120)
    elemento = wait.until(lambda driver: driver.find_element(By.XPATH, xpath1))

# numero = "459999999"
# mensagem = "Olá, estou enviando esta mensagem via Selenium!"
 
def mandar_mensagem(driver, numero, mensagem):
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
 
    driver.get(link)

    wait = WebDriverWait(driver, timeout=120)
    
    # Espera até que o elemento seja visível na página
    
    elemento = wait.until(lambda driver: driver.find_element(By.XPATH, xpath))
    driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
    print('Mensagem Enviada!')

def fechar_navegador(driver):
    input("Fechar Navegador")
    driver.quit()

if __name__ == '__main__':
    driv = abrir_chrome()
    esperar_login(driv)
    nome = 'Nicolas'
    numero = '45999232707'
    divida = 500
    mandar_mensagem(driv, nome, numero, divida )