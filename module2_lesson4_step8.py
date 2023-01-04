import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()

    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    res = log(abs(12 * sin(x)))

    input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_answer.send_keys(str(res))

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    button.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
