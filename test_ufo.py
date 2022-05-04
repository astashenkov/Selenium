from selenium.webdriver.common.by import By
import pytest
import time
import math


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ])
def test_find_ufo_breadcrumbs(browser, link):
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element(By.TAG_NAME, 'textarea').send_keys(str(math.log(int(time.time()))))
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    hint = browser.find_element(By.CSS_SELECTOR, '.smart-hints__feedback').text
    assert hint == 'Correct!'
