import pytest

from base_object.base import BaseObject
from base_object.locators import Locators as l
from base_object.assertion import Assertion
from pom.index_page import IndexPage


class MainPage(BaseObject, Assertion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_menu_button(self):
        self.to_click(l.MENU_BUTTON)

    def click_close_menu_button(self):
        self.to_click(l.CLOSE_MENU_BUTTON)

    def check_items(self):
        actual_text = self.is_visible(l.ALL_ITEMS_BUTTON).text
        expected_text = 'All Items'
        self.assertion(actual_text, expected_text)

    def check_about_link(self):
        actual_text = self.is_visible(l.ABOUT_LINK).text
        expected_text = 'About'
        self.assertion(actual_text, expected_text)

    def check_logout_link(self):
        actual_text = self.is_visible(l.LOGIN_BUTTON).text
        expected_text = 'Logout'
        self.assertion(actual_text, expected_text)

    def check_reset_link(self):
        actual_text = self.is_visible(l.RESET_APP_STATE).text
        expected_text = 'Reset App State'
        self.assertion(actual_text, expected_text)

    def check_closed_menu(self):
        actual_text = self.is_visible(l.TITLE_TEXT).text
        expected_text = 'PRODUCTS'
        self.assertion(actual_text, expected_text)


    #Параметризировали тесты выше



    def check_elements_list(self, locator, exp_text):
        actual_text = self.get_text(locator)
        expected_text = exp_text
        self.assertion(actual_text, expected_text)







