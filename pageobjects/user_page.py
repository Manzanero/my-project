from selenium.webdriver.common.by import By


class UserPage:

    # constructor
    def __init__(self, driver):
        self.driver = driver

        # elementos
        self.btn__logout = lambda: self.driver.find_element(By.CSS_SELECTOR, "#content > div > a")
