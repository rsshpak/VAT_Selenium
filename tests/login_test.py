import pytest
from pages.main_page import MainPage


@pytest.mark.usefixtures('login_fotrtlscm_sysadmin')
class TestW07FOTRTLSCM:
    def test_open_asset_manager_page(self, web_browser):
        page = MainPage(web_browser)
        page.wait_page_loaded(alert_text='Page is loaded')
        page.wait(2)
        page.screenshot('dashboard.png')
