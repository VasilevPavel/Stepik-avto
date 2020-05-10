from selenium import webdriver
import time
import math

def calc(a,b):
  return str(str((int(a)+int(b))))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element_by_xpath('//span[@id="num1"]')
    a = a_element.text
    print(a)

    b_element = browser.find_element_by_xpath('//span[@id="num2"]')
    b = b_element.text
    print(b)

    y = calc(a,b)
    print(y)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='" + y + "']").click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()