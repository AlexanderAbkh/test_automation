import pytest
from base_object.locators import *


def test_add_to_cart(authorized_page):
    authorized_page.click_add_back_pack()
    authorized_page.check_remove_btn()
    authorized_page.go_to_cart_list()
    authorized_page.check_back_title()









