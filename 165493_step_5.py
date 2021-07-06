from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    option1 = browser.find_element_by_css_selector(".form-check-custom > .form-check-label")
    option1.click()
    option2 = browser.find_element_by_xpath("//label[contains(.,'Robots rule')]")
    option2.click()
    option3 = browser.find_element_by_xpath("//button[contains(.,'Submit')]")
    option3.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
