import time

from selenium import webdriver
from selenium.webdriver.common.by import By

controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
controlador.get("https://www.udemy.com/join/login-popup/?next=/course/aprende-a-dominar-git-de-cero-a-experto/learn/lecture/15088334%3Fstart%3D0")

#Usando el atributo class de css
email = controlador.find_element(By.CSS_SELECTOR, "input.form-control")
email.send_keys("lesmes01@hotmail.com")

clave = controlador.find_element(By.CSS_SELECTOR, "input.textInput")
clave.send_keys("polomarco02*")

boton = controlador.find_element(By.CSS_SELECTOR,"input.btn-primary")
boton.click()
time.sleep(4)
controlador.quit()