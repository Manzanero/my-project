"""
ejercicio propuesto:

Imprimir por pantalla la temperatura en Madrid y añadir un mensaje indicando en cual de estas franjas está:
franja 1:  < 25ºC
franja 2:  25ºC < x < 30ºC
franja 3:  > 30ºC
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.temperature import Limites

driver = webdriver.Chrome()

try:
    driver.get("https://www.tiempo.com/madrid/hoy#:~:text=La%20previsi%C3%B3n%20del%20tiempo%20para,a%20los%2017%C2%B0C.")

    elemento_temperatura = driver.find_element(By.CSS_SELECTOR, "body > div.franjas > span.info-dia > span > p > span:nth-child(2)")
    temperatura_texto = elemento_temperatura.text

    temperatura_numero = int(temperatura_texto.rstrip('°C'))

    if temperatura_numero < Limites.LIMITE_1:
        print('franja 1')
    elif temperatura_numero > Limites.LIMITE_2:
        print('franja 3')
    else:
        print('franja 2')

except Exception:
    driver.save_screenshot('1.png')

finally:
    time.sleep(2)
    driver.quit()
