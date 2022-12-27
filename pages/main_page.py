from pages._base import WebPage
from pages._elements import WebElement
from locators.locators import MainPageLocators


class MainPage(WebPage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    pass
