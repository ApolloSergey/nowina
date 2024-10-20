from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    """
    Locators and actions of the Base Page
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=60, ignored_exceptions=[StaleElementReferenceException])
