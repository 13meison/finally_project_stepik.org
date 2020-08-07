from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(
            *ProductPageLocators.BTN_ADD_TO_BASKET)
        basket_link.click()
