from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_xpath_form')

    inputs = browser.find_elements(By.CSS_SELECTOR, 'input')
    for input in inputs:
        input.send_keys('Add some text to a form')

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
