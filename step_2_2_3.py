from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/selects1.html")
    time.sleep(1)
    x = int(browser.find_element_by_id("num1").text)
    y = int(browser.find_element_by_id("num2").text)
    sum_xy = str(int(x)+int(y))
    browser.find_element_by_tag_name("select").click()
    sum_opt = browser.find_element_by_css_selector("[value='{}']".format(sum_xy))
    sum_opt.click()
    browser.find_element_by_tag_name("button").click()
    time.sleep(5)
