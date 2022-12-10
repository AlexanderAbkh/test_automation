import pytest
import allure

@allure.description('Успешно залогинились валидными данными')
@allure.label('owner', 'Alex')
@allure.title('successfull login')
@allure.suite('Authorization')
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_login(index_page):
    with allure.step('entered username'):
        index_page.enter_user_name()
    with allure.step('entered password'):
        index_page.enter_password()
    with allure.step('clicked login button'):
        index_page.click_login_button()
    with allure.step('checked title on page'):
        index_page.check_title()


def test_unseccessful_login(index_page):
    index_page.enter_user_name()
    index_page.enter_incorrect_password()
    index_page.click_login_button()
    index_page.check_validation()


def test_logout(index_page):
    index_page.enter_user_name()
    index_page.enter_password()
    index_page.click_login_button()
    index_page.click_menu_button()
    index_page.click_logout_button()
    index_page.check_login_button()




