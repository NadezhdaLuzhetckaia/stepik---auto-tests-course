from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id("input_value").text
    ans = calc(x)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(ans)

    button = browser.find_element_by_tag_name("button")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)

    time.sleep(1)
