from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
page = 'http://suninjuly.github.io/math.html'

try:
    browser.get(page)
    input = browser.find_element_by_id('answer')
    x = int(browser.find_element_by_id('input_value').text)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    input.send_keys(calc(x))

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    time.sleep(5)

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
