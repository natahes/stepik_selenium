from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x = browser.find_element(By.ID, "input_value").text
    res = math.log(abs(12*math.sin(int(x))))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(res))

    browser.execute_script("window.scrollBy(0, 150);")

    for selector in ["#robotCheckbox", "#robotsRule", "button"]:
        input = browser.find_element(By.CSS_SELECTOR, selector)
        input.click()

finally:
    time.sleep(10)
    browser.quit()
