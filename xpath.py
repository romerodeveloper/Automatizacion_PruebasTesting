import time

from selenium import webdriver
from selenium.webdriver.common.by import By

controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
controlador.get("https://www.udemy.com/join/login-popup/?next=/course/aprende-a-dominar-git-de-cero-a-experto/learn/lecture/15088334%3Fstart%3D0")

#Uso de xpath por ruta relativa, si el componente cambia de lugar no hay problema. Mientras que el componente no cambie de valores
email = controlador.find_element(By.XPATH, "//input[@id='email--1']")
email.send_keys("lesmes01@hotmail.com")

clave = controlador.find_element(By.XPATH, "//input[@name='password']")
clave.send_keys("polomarco02*")

boton = controlador.find_element(By.XPATH,"//input[@name='submit']")
boton.click()
time.sleep(3)
controlador.quit()