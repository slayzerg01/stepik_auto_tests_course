from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

links = ["https://stepik.org/lesson/236897/step/1",
 "https://stepik.org/lesson/236898/step/1",
 "https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
 "https://stepik.org/lesson/236904/step/1",
 "https://stepik.org/lesson/236905/step/1"
    ]
# "https://stepik.org/lesson/236895/step/1",
# "https://stepik.org/lesson/236896/step/1",
# 

@pytest.mark.parametrize('url', links)
def test_guest_should_see_login_link(browser, url):
    link = f"{url}"
    browser.implicitly_wait(20)
    browser.get(link)

    button = browser.find_element(By.ID, "ember33")
    button.click()

    login_mail = browser.find_element(By.ID, 'id_login_email')
    login_mail.send_keys('bagdat250716@gmail.com')

    login_password = browser.find_element(By.ID, 'id_login_password')
    login_password.send_keys('bagdat7340')
    
    sign_button = browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader')
    sign_button.click()

    time.sleep(3)
    text_area = browser.find_element(By.CLASS_NAME, 'ember-text-area.ember-view.textarea.string-quiz__textarea')
    answer = str(math.log(int(time.time())))
    text_area.send_keys(answer)

    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
    submit_button.click()
    time.sleep(5)

    
    result_text_el = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    result_text = result_text_el.text
    print(result_text)

    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Correct!" == result_text, f"{result_text}"

    #
    time.sleep(5)
    