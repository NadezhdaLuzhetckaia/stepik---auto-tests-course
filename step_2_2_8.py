from selenium import webdriver
import time

import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/file_input.html")
    time.sleep(1)
    name = browser.find_element_by_css_selector("input[name='firstname']")
    name.send_keys("Boris")
    lname = browser.find_element_by_css_selector("input[name='lastname']")
    lname.send_keys("Demi")
    email = browser.find_element_by_css_selector("input[name='email']")
    email.send_keys("bor@cat.com")
    for_file = browser.find_element_by_css_selector("[type='file']")
    for_file.send_keys(file_path)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    time.sleep(10)