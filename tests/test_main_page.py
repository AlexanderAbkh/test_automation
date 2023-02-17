import time

import pytest
from base_object.locators import *


def test_add_to_cart(authorized_page):
    authorized_page.click_add_back_pack()
    authorized_page.check_remove_btn()
    authorized_page.go_to_cart_list()
    authorized_page.check_back_title()

def test_sorted_products(authorized_page):

    authorized_page.get_max_price()


def test_add_two_products(authorized_page):
    authorized_page.add_first_prod()
    authorized_page.check_first_num_in_inv()
    authorized_page.add_second_prod()
    authorized_page.check_sec_num_in_inv()

def test_remove_two_products(authorized_page):
    authorized_page.add_two_prods()
    authorized_page.remove_first_prod()
    authorized_page.check_first_remove()
    authorized_page.remove_sec_prod()

def test_check_add_btns_color(authorized_page):
    authorized_page.check_adds_btns_color()

def test_check_remove_btns_color(authorized_page):
    authorized_page.add_all_prods()
    authorized_page.check_remove_btns_color()


def test_check_products_are_sorted_correct_AtoZ(authorized_page):
    authorized_page.check_list_of_all_items_name_sortedAtoZ()

def test_check_products_are_sorted_correct_ZtoA(authorized_page):
    authorized_page.reverse_sortZtoA()
    authorized_page.check_list_of_all_items_name_sortedZtoA()


def test_check_products_are_sorted_correct_low_to_high(authorized_page):
    authorized_page.reverse_sort_low_to_high()
    authorized_page.check_list_of_all_items_name_sorted_low_to_high()

def test_check_removing_prods_from_shopcart(authorized_page):
    authorized_page.add_first_prod()
    authorized_page.go_to_my_prods()
    authorized_page.remove_prod_from_cart()
    authorized_page.back_to_shopping()
    authorized_page.check_removing()





def test_pesok(authorized_page):

    authorized_page.get_list_of_pricee()
    authorized_page.add_max_price()
