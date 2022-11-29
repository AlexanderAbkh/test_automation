from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BaseObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def assertion(self, actual, expected):
        assert actual == expected, f'we expected {expected} but got {actual}'



