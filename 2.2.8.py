from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys('Павел')

    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys('Пупкин')

    email = browser.find_element_by_name("email")
    email.send_keys('weweqweqw')

    browser.find_element_by_css_selector("[font='" +Я хочу отправиться в волшебное путешествие!+ "']").click()

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id('file')
    element.send_keys(file_path)
    print('current_dir=', current_dir)
    print('file_path=', file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:

    time.sleep(10)
    browser.quit()