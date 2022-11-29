from selenium.webdriver.common.by import By

class Locators:
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID,'password')
    LOGIN_BUTTON = (By.ID,'login-button')
    TITLE_TEXT = (By.CLASS_NAME, 'title')
    VALIDATION = (By.CSS_SELECTOR, '.error-message-container.error')