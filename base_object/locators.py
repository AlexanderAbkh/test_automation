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
    FIRST_BTN_ADD_TO_CARD = (By.ID, 'add-to-cart-sauce-labs-backpack')
    FIRST_BTN_REMOVE = (By.ID, 'remove-sauce-labs-backpack')
    SHOP_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    BACK_PACK_TITLE = (By.CLASS_NAME, 'inventory_item_name')
    ALL_PRODUCTS = (By.CSS_SELECTOR, '.inventory_list .inventory_item_name')







