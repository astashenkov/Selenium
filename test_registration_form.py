from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/registration1.html')

    inputs = browser.find_elements(By.CSS_SELECTOR, '.first_block input')
    for input in inputs:
        input.send_keys('Add some text')

    button = browser.find_element_by_class_name('btn')
    button.click()

    title = browser.find_element_by_name('h1')
    assert title.text == 'Congratulations! You have successfully registered!'


finally:
    time.sleep(10)
    browser.quit()