# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

TEXT_TO_FIND = "Make Appointment"

driver = webdriver.Chrome()  # abre un navegador chrome
driver.implicitly_wait(
    30
)  # si elemento no se encuentra esperar 30seg antes de dar la ejecucion por fallida para tener en cuneta las paginas lentas y la conexion de red que falla
# abre este sitio
driver.get("https://katalon-demo-cura.herokuapp.com/")
# Busca un elemento por su id y haz click sobre el
driver.find_element(By.ID, "btn-make-appointment").click()
# Busca el elemento por su id y limpia su valor
driver.find_element(By.ID, "txt-username").clear()
# escribe jhon doe
driver.find_element(By.ID, "txt-username").send_keys("John Doe")
# Busca el elemento por su id y limpia su valor
driver.find_element(By.ID, "txt-password").clear()
# escribe "ThisIsNotAPassword"
driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
# Busca un elemento por su id y haz click sobre el
driver.find_element(By.ID, "btn-login").click()
# Busca un elemento con este texto
text_found = (
    driver.find_element(By.XPATH, "//section[@id='appointment']/div/div/div/h2").text,
)
# Cierra en navegador
driver.quit()
