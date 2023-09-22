import time

from selenium import webdriver

from pageobjects.login_page import LoginPage
from pageobjects.user_page import UserPage

driver = webdriver.Chrome()

try:
    driver.get("http://the-internet.herokuapp.com/login")

    login_page = LoginPage(driver)
    user_page = UserPage(driver)

    login_page.tbx__username().send_keys("tomsmith")
    login_page.tbx__password().send_keys("SuperSecretPassword!")
    login_page.btn__login().click()
    es_visible = user_page.btn__logout().is_displayed()

    assert es_visible

finally:
    time.sleep(3)
    driver.quit()

