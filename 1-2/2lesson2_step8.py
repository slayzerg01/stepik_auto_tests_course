from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    #код, который заполняет обязательные поля
    text_field1 = browser.find_element(By.NAME, "firstname")
    text_field1.send_keys('Chel')

    text_field2 = browser.find_element(By.NAME, "lastname")
    text_field2.send_keys('Chelikov')

    text_field3 = browser.find_element(By.NAME, "email")
    text_field3.send_keys('Chel@mail.ru')

    file_path = os.path.join('C:/Users/Nitro/PycharmProjects/Selenium', 'file.txt')

    file_elem = browser.find_element(By.ID, 'file')
    file_elem.send_keys(file_path)

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