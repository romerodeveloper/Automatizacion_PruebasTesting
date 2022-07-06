
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
controlador.get("https://www.udemy.com/join/login-popup/?next=/course/aprende-a-dominar-git-de-cero-a-experto/learn/lecture/15088334%3Fstart%3D0")

usuario = controlador.find_element(By.NAME,"email")
clave = controlador.find_element(By.NAME,"password")

usuario.send_keys("lesmes01@hotmail.com")
clave.send_keys("polomarco02*")

boton = controlador.find_element(By.NAME,"submit")
boton.click()
time.sleep(5)
controlador.quit()
