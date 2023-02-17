import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pom.index_page import IndexPage
from pom.main_page import MainPage


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def index_page(setup):
    yield IndexPage(setup)


#зафикстурили тест (логин)
@pytest.fixture(scope='function')
def auth_setup(get_webdriver):
    driver = get_webdriver
    auth = IndexPage(driver)
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    auth.authorization()
    yield driver
    driver.quit()


@pytest.fixture
def authorized_page(auth_setup):
    yield MainPage(auth_setup)



@pytest.fixture(scope='function', autouse=True)
def screenshot_on_failures(setup, request):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        test_case_name = request.node.name
        screenshot = 'screenshot_on_failures' + f'_{test_case_name}' + '.png'
        setup.get_screenshot_as_file(screenshot)
        allure.attach.file(screenshot, 'screenshot_on_failures.png', attachment_type=allure.attachment_type.PNG)







