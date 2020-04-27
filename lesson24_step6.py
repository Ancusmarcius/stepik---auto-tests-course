from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, math


def calc(xer):
    return str(math.log(abs(12 * math.sin(int(xer)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()

    browser.get(link)
    price = browser.find_element_by_id("price")
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_id("book").click()
    browser.implicitly_wait(5)
    x = browser.find_element_by_id("input_value")
    f = calc(x.text)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(f)
    browser.find_element_by_id("solve").click()
    alert = browser.switch_to.alert
    # pyperclip.copy(alert.text.split(": ")[-1])
    print(alert.text.split(": ")[-1])



finally:
    time.sleep(10)
    browser.quit()
