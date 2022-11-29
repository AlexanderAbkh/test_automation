from base_object.base import BaseObject
from base_object.locators import Locators as l


class IndexPage(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_user_name(self):
        self.is_visible(l.USERNAME_FIELD).send_keys('standard_user')

    def enter_password(self):
        self.is_visible(l.PASSWORD_FIELD).send_keys('secret_sauce')

    def click_login_button(self):
        self.is_clickable(l.LOGIN_BUTTON).click()

    def check_title(self):
        actual_text = self.is_visible(l.TITLE_TEXT).text
        expected_text = 'PRODUCTS'
        self.assertion(actual_text, expected_text)

    def enter_incorrect_password(self):
        self.is_visible(l.PASSWORD_FIELD).send_keys('123456')

    def check_validation(self):
        actual_text = self.is_visible(l.VALIDATION).text
        expected_text = 'Epic sadface: Username and password do not match any user in this service'
        self.assertion(actual_text, expected_text)
















