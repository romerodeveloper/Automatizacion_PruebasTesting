import time

from selenium import webdriver
from selenium.webdriver.common.by import By

controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
controlador.get("https://www.udemy.com/join/login-popup/?next=/course/aprende-a-dominar-git-de-cero-a-experto/learn/lecture/15088334%3Fstart%3D0")

link_recuperacion = controlador.find_element(By.PARTIAL_LINK_TEXT,"¿Has")
link_recuperacion.click()

#El capcha no se puede automatizar
check = controlador.find_element(By.CLASS_NAME, "check")
check.click()

correo = controlador.find_element(By.ID, "form-element--1")
correo.send_keys("dfdflujogramas@gmail.com")
time.sleep(1)








time.sleep(5)
