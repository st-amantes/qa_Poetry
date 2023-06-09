import allure
from selene import browser
from selene.support.conditions.have import exact_text

from poetry_env.pages.page_reg import BasePageRegisterNumber



@allure.title("Тест на регистрацию через кнопку 'Войти' по номеру")
def test_registration_number():
    basepage = BasePageRegisterNumber()
    browser.open('')
    basepage.button_in()
    basepage.button_reg()
    basepage.button_number()
    basepage.send_number()
    basepage.send_sms()
    basepage.password_input()
    basepage.button_in_click()