from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

    loginpage = LoginPage(browser, link)
    loginpage.should_be_login_page()
