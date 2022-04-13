from selenium import webdriver
import time
import os

try:
    page = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(page)

    name = browser.find_element_by_css_selector('[name="firstname"]')
    name.send_keys('Stephen')
    surname = browser.find_element_by_css_selector('[name="lastname"]')
    surname.send_keys('Hawking')
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('email@email.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_example.txt')
    browser.find_element_by_id('file').send_keys(file_path)

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
