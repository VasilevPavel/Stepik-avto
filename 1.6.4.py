from selenium import webdriver
import time

link = " http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input.form-control")
    input1.send_keys("Мой")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Первый")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Автотест")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("На Python")

    #button=browser.find_elements_by_by_xpath("[button//type='submit']")
    #button.click()
    button = browser.find_element_by_xpath('//button[type="submit"]')
    button.click()
    #elements = browser.find_elements_by_tag_name("button")
    # for element in elements:
    #   if browser.find_elements_by_by_xpath("[//type='submit']"):
    #       button.click()


finally:

    time.sleep(10)
    browser.quit()
