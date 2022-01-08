from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def click_btn():
    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
    btn = browser.find_element(By.ID, "book")
    btn.click()

    x = browser.find_element(By.ID, "input_value").text
    res = math.log(abs(12*math.sin(int(x))))
    print(x, res)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(res))

    btn = browser.find_element(By.ID, "solve")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
