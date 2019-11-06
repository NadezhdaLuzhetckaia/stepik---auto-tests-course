from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/get_attribute.html")
    time.sleep(1)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")

    ans = calc(x)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(ans)
    time.sleep(1)
    robot_check = browser.find_element_by_id("robotCheckbox")
    robot_check.click()
    robot_radio = browser.find_element_by_id("robotsRule")
    robot_radio.click()
    button = browser.find_element_by_class_name("btn-default")
    button.click()
    time.sleep(5)