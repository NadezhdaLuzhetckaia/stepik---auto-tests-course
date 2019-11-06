from selenium import webdriver
import time

import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    time.sleep(1)

    x = browser.find_element_by_id("input_value").text
    ans = calc(x)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(ans)

    robot_check = browser.find_element_by_id("robotCheckbox")

    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_check)

    robot_check.click()
    robot_radio = browser.find_element_by_id("robotsRule")
    robot_radio.click()

    button = browser.find_element_by_tag_name("button")

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # browser.execute_script("window.scrollBy(0, 100);")
    time.sleep(1)
    button.click()
    time.sleep(10)
