from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
page = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser.get(page)
    input = browser.find_element_by_id('answer')
    x = int(browser.find_element_by_id('treasure').get_attribute('valuex'))

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    input.send_keys(calc(x))

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
