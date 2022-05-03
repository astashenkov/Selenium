import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    link = 'https://www.google.com/'
    browser.get(link)
    yield browser
    time.sleep(10)
    print('Test has done.')
    browser.quit()


def test_gpage(browser):
    input_fild = browser.find_element(By.CSS_SELECTOR, '.gLFyf.gsfi')
    input_fild.send_keys('Hello, World!')
    button = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
    button.submit()
