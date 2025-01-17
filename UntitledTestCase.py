# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.find_element(By.ID, "btn-make-appointment").click()
        driver.find_element(By.ID, "txt-username").clear()
        driver.find_element(By.ID, "txt-username").send_keys("John Doe")
        driver.find_element(By.ID, "txt-password").clear()
        driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
        driver.find_element(By.ID, "btn-login").click()
        self.assertEqual(
            "Make Appointment",
            driver.find_element(
                By.XPATH, "//section[@id='appointment']/div/div/div/h2"
            ).text,
        )

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
