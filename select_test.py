from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    browser = webdriver.Chrome()
    page = 'http://suninjuly.github.io/selects1.html'
    browser.get(page)

    browser.execute_script('{document.querySelector("button").style.backgroundColor="yellow";}')
    time.sleep(2)

    sum = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)
    select = Select(browser.find_element_by_css_selector('#dropdown'))
    select.select_by_value(str(sum))

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
