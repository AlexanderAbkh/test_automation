import pytest


def test_successful_login(index_page):
    index_page.enter_user_name()
    index_page.enter_password()
    index_page.click_login_button()
    index_page.check_title()


def test_unseccessful_login(index_page):
    index_page.enter_user_name()
    index_page.enter_incorrect_password()
    index_page.click_login_button()
    index_page.check_validation()


@pytest.mark.api
def test_api():
    assert 1 == 1


@pytest.mark.ui
def test_ui():
    assert 1 == 1


@pytest.mark.smoke
@pytest.mark.ui
def test_smoke():
    assert 1 == 1
