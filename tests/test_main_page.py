import pytest
from base_object.locators import *


case_1 = [Locators.ALL_ITEMS_BUTTON, 'All Items',]
case_2 = [Locators.ABOUT_LINK, 'About', ]
case_3 = [Locators.LOGIN_BUTTON, 'Logout', ]
case_4 = [Locators.RESET_APP_STATE, 'Reset App State', ]


@pytest.mark.parametrize('locator, exp_text', (case_1, case_2, case_3, case_4))
def test_test(authorized_page, locator, exp_text):
    authorized_page.click_menu_button()
    authorized_page.check_elements_list(locator, exp_text)
    authorized_page.click_close_menu_button()




