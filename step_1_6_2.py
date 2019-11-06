from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    time.sleep(5)
    # button = browser.find_element_by_id("submit_button")
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(5)