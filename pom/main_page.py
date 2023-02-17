import time

import pytest

from base_object.base import BaseObject
from base_object.locators import Locators as l
from base_object.assertion import Assertion
from pom.index_page import IndexPage
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class MainPage(BaseObject, Assertion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_menu_button(self):
        self.to_click(l.MENU_BUTTON)

    def click_close_menu_button(self):
        self.to_click(l.CLOSE_MENU_BUTTON)


    def check_remove_btn(self):
        exp_text = 'REMOVE'
        actual_text = self.get_text(l.FIRST_BTN_REMOVE)
        self.assertion_equal(actual_text, exp_text)

    def go_to_cart_list(self):
        self.to_click(l.SHOP_CART_LINK)

    def check_back_title(self):
        exp_text = 'Sauce Labs Backpack'
        actual_text = self.get_text(l.ALL_ITEMS_NAMES)
        self.assertion_equal(actual_text, exp_text)

    def get_list_of_price(self):
        prices_products = self.are_visible(l.ALL_PRICES)
        list_of_prices_products = []

        for i in prices_products:
            text = i.text
            list_of_prices_products.append(text)


        list_prices = []

        for i in list_of_prices_products:
            list_prices.append(i.replace("$", ""))
            return list_prices







    def add_first_prod(self):
        self.to_click(l.ADD_FIRST_PROD)


    def check_first_num_in_inv(self):
        num_in_inv = int(self.is_visible(l.VALUE_OF_PRODUCTS_IN_INV).text)
        exp_num = 1
        self.assertion_equal(num_in_inv, exp_num)



    def add_second_prod(self):
        self.to_click(l.ADD_SEC_PROD)

    def check_sec_num_in_inv(self):
        num_in_inv = int(self.is_visible(l.VALUE_OF_PRODUCTS_IN_INV).text)
        exp_num = 2
        self.assertion_equal(num_in_inv, exp_num)

    def add_two_prods(self):
        self.to_click(l.ADD_FIRST_PROD)
        self.to_click(l.ADD_SEC_PROD)


    def remove_first_prod(self):
        self.to_click(l.FIRST_REMOVE_BTN)


    def remove_sec_prod(self):
        self.to_click(l.SECOND_REMOVE_BTN)


    def check_first_remove(self):
        num_in_inv = int(self.is_visible(l.VALUE_OF_PRODUCTS_IN_INV).text)
        exp_num = 1
        self.assertion_equal(num_in_inv, exp_num)


    def check_sec_remove(self):
        pass


    def check_add_btns_color(self):
        adds = self.are_visible(l.All_BTNS_ADD_TO_CART)
        exp_color = 'rgba(226, 35, 26, 1)'

        for i in adds:
            i = self.to_get_color(l.All_BTNS_ADD_TO_CART)
            self.assertion_equal(i, exp_color)


    def add_all_prods(self):
        all_prods = self.are_visible(l.All_BTNS_ADD_TO_CART)

        for i in all_prods:
            i.click()



    def check_remove_btns_color(self):
        removes = self.are_visible(l.ALL_REMOVES_BTNS)
        exp_color = 'rgba(71, 76, 85, 1)'

        for i in removes:
            i = self.to_get_color(l.ALL_REMOVES_BTNS)
            self.assertion_equal(i, exp_color)



    def check_sort_a_to_z(self):
        text = self.is_visible(l.SELECT_SORT).text[0:13:]
        exp_text = 'Name (A to Z)'
        self.assertion_equal(text, exp_text)




    def check_list_of_all_items_name_sortedAtoZ(self):
        all_names = self.are_visible(l.ALL_ITEMS_NAMES)
        list_of_names = []

        for i in all_names:
            text = i.text
            list_of_names.append(text)
            return list_of_names


        sorted_list = list_of_names.sort()

        self.assertion_equal(list_of_names, sorted_list)


    def open_sort_selector(self):
        self.to_click(l.SELECT_SORT)


    def reverse_sortZtoA(self):
        dropdown = self.is_visible(l.SELECT_SORT)
        select = Select(dropdown)
        select.select_by_visible_text('Name (Z to A)')


    def reverse_sort_low_to_high(self):
        dropdown = self.is_visible(l.SELECT_SORT)
        select = Select(dropdown)
        select.select_by_visible_text('Price (low to high)')

    def reverse_sort_high_to_low(self):
        dropdown = self.is_visible(l.SELECT_SORT)
        select = Select(dropdown)
        select.select_by_visible_text('Price (high to low)')


    def check_list_of_all_items_name_sortedZtoA(self):
        all_names = self.are_visible(l.ALL_ITEMS_NAMES)
        list_of_names = []

        for i in all_names:
            text = i.text
            list_of_names.append(text)
            return list_of_names

        reverse_list = list_of_names.reverse()

        self.assertion_equal(list_of_names, reverse_list)


    def check_list_of_all_items_name_sorted_low_to_high(self):

        prices_products = self.are_visible(l.ALL_PRICES)
        list_of_prices_products = []

        for i in prices_products:
            text = i.text
            list_of_prices_products.append(text)

        list_prices = []

        for i in list_of_prices_products:
            list_prices.append(i.replace("$", ""))
            return list_prices

        reverse_list = list_prices.reverse()

        self.assertion_equal(list_prices, reverse_list)



    def go_to_my_prods(self):
        self.to_click(l.SHOP_CART_LINK)

    def remove_prod_from_cart(self):
        self.to_click(l.BTN_OF_REMOVING_FROM_CART)

    def back_to_shopping(self):
        self.to_click(l.BACK_TO_SHOP)

    def check_removing(self):
        self.is_visible(l.ADD_FIRST_PROD)

    def get_list_of_pricee(self):

        prices_products = self.are_visible(l.ALL_PRICES)
        list = []
        for i in prices_products:
            text = i.text
            list.append(text)



        list_2 = []

        for i in list:
            list_2.append(i.replace("$", ""))

        self.nums = [float(s) for s in list_2]
        return self.nums

    def add_max_price(self):
        max_price = max(self.nums)
        ADD_MAX_PRICE = (By.XPATH, f"//*[@class='inventory_item_price' and text()={max_price}]/../button")
        self.to_click(ADD_MAX_PRICE)
        time.sleep(5)


































"""
    def xxx(self):
        global xvalue
        xvalue = get_sth()
        return xvalue"""
















