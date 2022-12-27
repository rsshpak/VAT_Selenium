from selenium.webdriver.common.by import By


class LoginPageLocators:
    CUSTOMER_INPUT = (By.CSS_SELECTOR, '#Customer')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#UserName')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#Password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '#LoginButton')


class MainPageLocators:
    pass
