from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    page = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(page)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_id('book').click()
    browser.execute_script('window.scrollBy(0, 400);')

    x = int(browser.find_element_by_id('input_value').text)
    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))

    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(5)
    browser.quit()