from selenium import webdriver
import time
import math


try:
    browser = webdriver.Chrome()
    browser.get( "http://suninjuly.github.io/find_link_text")

    a = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link = browser.find_element_by_link_text(a)
    link.click()
   
    input1 = browser.find_element_by_tag_name("input.form-control")
    input1.send_keys("Мой")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Первый")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Автотест")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("На Python")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    time.sleep(10)
    browser.quit()