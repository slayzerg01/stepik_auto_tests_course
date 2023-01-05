from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    #код, который заполняет обязательные поля

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")  
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x) 
    
    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(y)
    
    button = browser.find_element(By.TAG_NAME, "button")  
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()