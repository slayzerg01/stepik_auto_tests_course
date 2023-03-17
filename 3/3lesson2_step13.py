import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def chek_browser(link):
    browser = webdriver.Chrome()
    browser.get(link)

    #код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class input")
    input3.send_keys("mail@box.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.quit()

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        chek_browser("http://suninjuly.github.io/registration1.html")
        
      
    def test_abs2(self):
        chek_browser("http://suninjuly.github.io/registration2.html")
        
        
if __name__ == "__main__":
    unittest.main()
