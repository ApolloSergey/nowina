import logging

from utils.tools.logs import log
from utils.helpers.config_provider import settings_config
from utils.helpers.common_actions import CommonActions
from seleniumbase import Driver
from utils.tools.singleton import singleton


@singleton
class Browser(object):

    def set_browser(self):
        driver = None
        browser = settings_config.browser
        if browser == "":
            browser = None
        log.info("Browser: " + browser)
        if browser == "chrome" or browser is None:
            driver = Driver(browser="chrome", headless=CommonActions.strtobool(settings_config.chrome_headless_mode))
        if browser == "firefox":
            driver = Driver(browser="firefox")
        driver.maximize_window()
        return driver

    def get_browser(self):
        return self.set_browser()

    def open_webpage(self, driver, url):
        logging.info("Open web page: %s", str(url))
        driver.get(url)
        logging.debug("Web page has been opened")

    def close(self, driver):
        log.info("Close browser")
        driver.quit()

    def refresh_browser(self, driver):
        driver.refresh()

    def open_base_page(self, driver):
        """
        Open useInsider page
        """
        self.open_webpage(driver, settings_config.base_page_url)


browser_element = Browser()
