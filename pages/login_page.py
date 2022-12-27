from pages._base import WebPage
from pages._elements import WebElement
from locators.locators import LoginPageLocators


class LoginPage(WebPage):
    def __init__(self, web_driver):
        super().__init__(web_driver)

    customer_input = WebElement(*LoginPageLocators.CUSTOMER_INPUT)
    username_input = WebElement(*LoginPageLocators.USERNAME_INPUT)
    password_input = WebElement(*LoginPageLocators.PASSWORD_INPUT)
    sign_in_button = WebElement(*LoginPageLocators.SIGN_IN_BUTTON)
