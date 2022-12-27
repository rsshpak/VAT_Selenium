from selenium import webdriver
from pages.login_page import LoginPage
from test_data.authorization import DefaultSupervisorData
from test_data.authorization import FotrtlscmuSysadminData
import pytest
import os

link = 'https://tvaweb07.radiantrfid.com/VATPortal/'


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome', help='Select env')


@pytest.fixture(scope='class')
def web_browser(request):

    browser_name = request.config.getoption('browser_name')

    if browser_name == 'Chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('start-maximized')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--log-level=DEBUG')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # chrome_options.add_argument('--headless')

        prefs = {'download.default_directory': (os.getcwd() + r'\test_data').replace('/', '\''),
                 'download.prompt_for_download': False,
                 'download.directory_upgrade': True,
                 'safebrowsing.enabled': False,
                 }
        chrome_options.add_experimental_option("prefs", prefs)

        browser = webdriver.Chrome(options=chrome_options)
        browser.get(link)

        yield browser
        browser.quit()

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")


@pytest.fixture(scope='class')
def login_default_supervisor(web_browser):
    """ Authorization by Default Supervisor. """

    login_page = LoginPage(web_browser)
    login_page.wait_page_loaded()
    login_page.customer_input.send_keys(DefaultSupervisorData.CUSTOMER)
    login_page.username_input.send_keys(DefaultSupervisorData.USERNAME)
    login_page.password_input.send_keys(DefaultSupervisorData.PASSWORD)
    login_page.sign_in_button.click()
    login_page.wait_page_loaded()


@pytest.fixture(scope='class')
def login_fotrtlscm_sysadmin(web_browser):
    """ Authorization by Customer Sysadmin. """

    login_page = LoginPage(web_browser)
    login_page.wait_page_loaded()
    login_page.customer_input.send_keys(FotrtlscmuSysadminData.CUSTOMER)
    login_page.username_input.send_keys(FotrtlscmuSysadminData.USERNAME)
    login_page.password_input.send_keys(FotrtlscmuSysadminData.PASSWORD)
    login_page.sign_in_button.click()
    login_page.wait_page_loaded()
