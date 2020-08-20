from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(
            *ProductPageLocators.BTN_ADD_TO_BASKET)
        basket_link.click()

    def should_be_field_price(self):
        field_price = self.browser.find_element(
            *ProductPageLocators.FIELD_PRICE)
        text_field_price = field_price.text
        assert self.is_element_present(
            *ProductPageLocators.FIELD_PRICE), 'price field not found'
        # реализуйте проверку, что есть форма логина

    def should_be_field_name_product(self):
        field_name_product = self.browser.find_element(
            *ProductPageLocators.FIELD_NAME_PRODUCT)
        text_field_name_product = field_name_product.text
        assert self.is_element_present(
            *ProductPageLocators.FIELD_NAME_PRODUCT), 'field name product not found'

    def field_matching_check_name(self):
        alert_name = self.browser.find_elements(
            By.CSS_SELECTOR, "#messages .alertinner > strong")
        text_alert_name = alert_name[0].text
        text_alert_price = alert_name[2].text
        assert text_alert_name == text_field_name_product, "jopa"
        assert text_alert_price == text_field_price, "xyuiuyiu"
        # assert *ProductPageLocators.FIELD_NAME_PRODUCT.text == text_alert_name, 'field name product not found'
