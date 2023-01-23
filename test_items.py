import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_product_page_on_website_contains_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    try:
        result = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    except NoSuchElementException:
        result = None

    assert result is not None, "button not found"
