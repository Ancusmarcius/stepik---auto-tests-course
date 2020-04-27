from selenium import webdriver
import time
import math



def calc(xer):
    return str(math.log(abs(12 * math.sin(int(xer)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value")
    f = calc(x.text)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(f)
    btn = browser.find_element_by_css_selector("button.btn")
    btn.click()


    alert = browser.switch_to.alert
    print(alert.text.split(": ")[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
