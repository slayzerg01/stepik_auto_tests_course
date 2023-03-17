from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #код, который заполняет обязательные поля
    x1 = int(browser.find_element(By.ID, 'num1').text)
    x2 = int(browser.find_element(By.ID, 'num2').text)
    y = x1 + x2
    print(y)
    select_elem = browser.find_element(By.CLASS_NAME, 'custom-select')

    Select(select_elem).select_by_value(str(y))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()