from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class TestSuites(unittest.TestCase):
    def test_first_form(self):
        browser = webdriver.Chrome()
        page = 'http://suninjuly.github.io/registration1.html'
        browser.get(page)

        input_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        input_surname = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        input_email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')

        input_name.send_keys('Some name')
        input_surname.send_keys('Some surname')
        input_email.send_keys('Some email')

        button = browser.find_element(By.CSS_SELECTOR, '.btn')
        button.click()

        time.sleep(1)

        title = browser.find_element(By.TAG_NAME, 'h1')
        self.assertEqual(title.text, 'Congratulations! You have successfully registered!')

        browser.quit()

    def test_second_form(self):
        browser = webdriver.Chrome()
        page = 'http://suninjuly.github.io/registration2.html'
        browser.get(page)

        input_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        input_surname = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        input_email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')

        input_name.send_keys('Some name')
        input_surname.send_keys('Some surname')
        input_email.send_keys('Some email')

        button = browser.find_element(By.CSS_SELECTOR, '.btn')
        button.click()

        title = browser.find_element(By.TAG_NAME, 'h1')
        self.assertEqual(title.text, 'Congratulations! You have successfully registered!weces')

        browser.quit()


if __name__ == '__main__':
    TestSuites.test_first_form()
    TestSuites.test_second_form()
