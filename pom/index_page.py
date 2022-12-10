from base_object.base import BaseObject
from base_object.locators import Locators as l
from base_object.assertion import Assertion


class IndexPage(BaseObject, Assertion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def authorization(self):
        self.enter_user_name()
        self.enter_password()
        self.click_login_button()

    def enter_user_name(self):
        self.to_text(l.USERNAME_FIELD, 'standard_user')

    def enter_password(self):
        self.to_text(l.PASSWORD_FIELD, 'secret_sauce')

    def enter_incorrect_password(self):
        self.to_text(l.PASSWORD_FIELD, '123456')

    def click_login_button(self):
        self.to_click(l.LOGIN_BUTTON)


    def click_menu_button(self):
        self.to_click(l.MENU_BUTTON)

    def click_logout_button(self):
        self.to_click(l.LOGOUT_BUTTON)

    def check_title(self):
        actual_text = self.get_text(l.TITLE_TEXT)
        expected_text = 'PRODUCTS'
        self.assertion(actual_text, expected_text)

    def check_login_button(self):
        actual_result = self.to_get_attribute(l.LOGIN_BUTTON, 'value')
        expected_result = 'Login'
        self.assertion(actual_result, expected_result)

    def check_validation(self):
        actual_text = self.get_text(l.VALIDATION)
        expected_text = 'Epic sadface: Username and password do not match any user in this service'
        self.assertion(actual_text, expected_text)


