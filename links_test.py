from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    page = 'http://suninjuly.github.io/find_link_text'
    browser.get(page)

    locator = math.ceil(math.pow(math.pi, math.e)*10000)
    link = browser.find_element_by_partial_link_text(str(locator))
    link.click()

    first_name = browser.find_element_by_name('first_name')
    first_name.send_keys('Edwin')

    last_name = browser.find_element_by_name('last_name')
    last_name.send_keys('Olsson')

    city = browser.find_element_by_class_name('city')
    city.send_keys('Stockholm')

    country = browser.find_element_by_id('country')
    country.send_keys('Sweden')
    
    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
