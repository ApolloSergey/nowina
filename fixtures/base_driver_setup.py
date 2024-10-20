import pytest

from utils.helpers.config_provider import settings_config
from utils.browser import Browser
from utils.helpers.ui_helper import UiHelper
from utils.tools.logs import log


@pytest.fixture()
def driver_setup(request):
    test_name = request.node.test_name_
    log.info("Start test: {}".format(test_name))
    browser = Browser()
    driver = browser.get_browser()
    driver.get(settings_config.base_page_url)
    request.cls.driver = driver
    yield
    if request.node.rep_setup.failed or request.node.rep_call.failed:
        try:
            UiHelper.create_screen_shot(driver, test_name)
        except Exception as e:
            log.error("Could not create screen_shot . Error: {}. ".format(e))
    driver.quit()
