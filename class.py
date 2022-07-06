
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
controlador.get("https://www.udemy.com/join/login-popup/?next=/course/aprende-a-dominar-git-de-cero-a-experto/learn/lecture/15088334%3Fstart%3D0")

email = controlador.find_element(By.CLASS_NAME,"form-control")
clave = controlador.find_element(By.CLASS_NAME,"textinput")

email.send_keys("lesmes01@hotmail.com")
clave.send_keys("polomarco02*")

boton = controlador.find_element(By.CLASS_NAME, "btn-primary ")
boton.click()
time.sleep(5)
controlador.quit()
