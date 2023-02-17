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
    FIRST_BTN_REMOVE = (By.ID, 'remove-sauce-labs-backpack')
    SHOP_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    ALL_ITEMS_NAMES = (By.CLASS_NAME, 'inventory_item_name')
    ALL_PRICES = (By.CSS_SELECTOR, '.inventory_item_price')
    All_BTNS_ADD_TO_CART = (By.CSS_SELECTOR, '.btn.btn_primary.btn_small.btn_inventory')
    VALUE_OF_PRODUCTS_IN_INV = (By.CSS_SELECTOR, '.shopping_cart_badge')
    ADD_FIRST_PROD = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_SEC_PROD = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    FIRST_REMOVE_BTN = (By.ID, 'remove-sauce-labs-backpack')
    SECOND_REMOVE_BTN = (By.ID, 'remove-sauce-labs-bike-light')
    ALL_REMOVES_BTNS = (By. CSS_SELECTOR, '.btn.btn_secondary.btn_small.btn_inventory')
    SELECT_SORT = (By.CLASS_NAME, 'product_sort_container')
    BTN_OF_REMOVING_FROM_CART = (By.ID, 'remove-sauce-labs-backpack')
    BACK_TO_SHOP = (By.ID, 'continue-shopping')











