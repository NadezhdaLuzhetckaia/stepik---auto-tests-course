from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element_by_id("book")
    button.click()

    x = browser.find_element_by_id("input_value").text
    ans = calc(x)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(ans)

    button = browser.find_element_by_id("solve")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)