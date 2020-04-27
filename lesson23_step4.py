from selenium import webdriver
import time
import math
import pyperclip


def calc(xer):
    return str(math.log(abs(12 * math.sin(int(xer)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id("input_value")
    f = calc(x.text)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(f)
    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()
    alert = browser.switch_to.alert
    pyperclip.copy(alert.text.split(": ")[-1])
    print(alert.text.split(": ")[-1])

finally:

    time.sleep(1)

    browser.quit()
