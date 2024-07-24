from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

xpath = "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"

driver.get("https://web.whatsapp.com/")

input("CONFIRMAR 1")
numero = "556791260268"
mensagem = "Olá, estou enviando esta mensagem via Selenium!"
link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"

driver.get(link)

cookies = driver.get_cookies()
print(cookies)

input('Confirmar 2')
driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)

input("Confirmar 3")
driver.quit()

