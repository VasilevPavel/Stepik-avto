from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


button1 = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"),'100'))

button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
otvet = browser.find_element_by_id("answer")
otvet.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()

time.sleep(10)
browser.quit()