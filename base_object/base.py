"""
Base Modul
"""
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from support.logger import *
import logging as log
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from typing import List # необходимый импорт



class BaseObject:
    log = log_method(logLevel=log.INFO)
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):

        """
        TODO: under discussion
        This method helps us to find visible element
        :param locator: locator to find element
        :return: visible element
        """
        self.log.info(f'element {locator} is visible')
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))



    def to_click(self, locator):
        self.is_clickable(locator).click()

    def to_text(self, locator, text):
        self.is_visible(locator).send_keys(text)

    def get_text(self, locator):
        return self.is_visible(locator).text


    def to_get_attribute(self, locator, attribute):
        return self.is_visible(locator).get_attribute(attribute)

    def are_visible(self, locator) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located(locator))


    def scroll(self, locator):
        actions = ActionChains(self.driver)  # создаем экземпляр класса, а driver - это экземпляр вебдрайвера.
        element = locator  # находим элемент
        actions.move_to_element(element).perform()








