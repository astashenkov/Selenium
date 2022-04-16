from selenium import webdriver
import time
import math

try:
    page = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(page)
    browser.find_element_by_css_selector('.btn').click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element_by_id('input_value').text)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_css_selector('.btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()