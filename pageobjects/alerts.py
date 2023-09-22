from selenium.webdriver.common.by import By


class AlertsPage:

    def __init__(self, driver):
        self.driver = driver
        self.btn__simple = lambda: self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button")
        self.btn__ad = lambda: self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button")
        self.result = lambda: self.driver.find_element(By.ID, "result")
