from selenium.webdriver.common.by import By

class Locators:
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID,'password')
    LOGIN_BUTTON = (By.ID,'login-button')
    TITLE_TEXT = (By.CLASS_NAME, 'title')
    VALIDATION = (By.CSS_SELECTOR, '.error-message-container.error')
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    CLOSE_MENU_BUTTON = (By.ID, 'react-burger-cross-btn')
    ALL_ITEMS_BUTTON = (By.ID, 'inventory_sidebar_link')
    ABOUT_LINK = (By.ID, 'about_sidebar_link')
    RESET_APP_STATE = (By.ID, 'reset_sidebar_link')
    btns = (By.CSS_SELECTOR, '.btn.btn_primary.btn_small.btn_inventory')



