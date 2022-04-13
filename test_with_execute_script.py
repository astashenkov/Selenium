from selenium import webdriver
import math
import time

try:
    page = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(page)

    x = int(browser.find_element_by_id('input_value').text)
    def calc(x):
        return str(math.log( abs( 12 * math.sin(x) ) ))

    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.execute_script('return window.scrollBy(0, 200);')

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
