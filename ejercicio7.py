import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_accept(self):
        try:
            self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
            self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button").click()
            alert = self.driver.switch_to.alert
            alert.accept()
            assert self.driver.find_element(By.ID, "result").text == "You successfully clicked an alert"

        finally:
            pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()