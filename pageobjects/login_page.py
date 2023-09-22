from selenium.webdriver.common.by import By


class LoginPage:

    # constructor
    def __init__(self, driver):
        self.driver = driver

        # elementos
        self.tbx__username = lambda: self.driver.find_element(By.ID, "username")
        self.tbx__password = lambda: self.driver.find_element(By.ID, "password")
        self.btn__login = lambda: self.driver.find_element(By.CSS_SELECTOR, "#login > button")
