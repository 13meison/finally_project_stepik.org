from pages.product_page import ProductPage
from pages.product_page import BasePage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    stepik_function_assert = BasePage(browser, link)
    stepik_function_assert.solve_quiz_and_get_code()
