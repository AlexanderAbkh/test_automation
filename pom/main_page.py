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

    def click_add_back_pack(self):
        self.to_click(l.FIRST_BTN_ADD_TO_CARD)

    def check_remove_btn(self):
        exp_text = 'REMOVE'
        actual_text = self.get_text(l.FIRST_BTN_REMOVE)
        self.assertion(actual_text, exp_text)

    def go_to_cart_list(self):
        self.to_click(l.SHOP_CART_LINK)


    def check_back_title(self):
        exp_text = 'Sauce Labs Backpack'
        actual_text = self.get_text(l.BACK_PACK_TITLE)
        self.assertion(actual_text, exp_text)


    def get_sorted_products(self):
        sorted_products = self.are_visible(l.ALL_PRODUCTS)
        list_of_products = []

        for i in sorted_products:
            text = i.text
            list_of_products.append(text)
        print(list_of_products)
        return list_of_products
































