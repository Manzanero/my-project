import json
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

URL_DATOS = "https://faas-fra1-afec6ce7.doserverless.co/api/v1/web/fn-1f1056ff-de8e-4509-9811-27a68419f504/test/test"
URL = "https://the-internet.herokuapp.com/checkboxes"

for i in range(10):
    response = requests.get(URL_DATOS)
    print("intento: ", i)
    try:
        valor_check1 = response.json()["checkbox 1"]
        valor_check2 = response.json()["checkbox 2"]
        break
    except json.decoder.JSONDecodeError:
        pass

else:
    raise Exception("demasiados intentos")


def checkboxes(check1, check2):
    driver = webdriver.Chrome()

    try:
        driver.get(URL)

        checks = driver.find_elements(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]")
        chk__check1 = checks[0]
        chk__check2 = checks[1]

        chk__check1_checked = chk__check1.is_selected()
        chk__check2_checked = chk__check2.is_selected()

        if (chk__check1_checked and not check1) or (not chk__check1_checked and check1):
            chk__check1.click()
        if (chk__check2_checked and not check2) or (not chk__check2_checked and check2):
            chk__check2.click()

    finally:
        time.sleep(1)
        driver.quit()


checkboxes(valor_check1, valor_check2)
# checkboxes(True, False)
# checkboxes(False, True)
# checkboxes(False, False)
