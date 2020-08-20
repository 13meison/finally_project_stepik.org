from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    FIELD_PRICE = (By.CSS_SELECTOR, "p.price_color")
    FIELD_NAME_PRODUCT = (By.CSS_SELECTOR, "h1")
    FIELD_PRICE_ALERT = (By.CSS_SELECTOR, "p.price_color")
    FIELD_NAME_PRODUCT_ALERT = (By.CSS_SELECTOR, "h1")

    # ALERT_INNER_NAME = (By.CSS_SELECTOR, "#messages .alertinner")
    # ALERT_INNER_PRICE = (
    #     By.CSS_SELECTOR, ".#messages:last-child .alertinner")
