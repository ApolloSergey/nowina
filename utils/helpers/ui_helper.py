from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import os
from datetime import datetime

from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from project_constants import project_path


class UiHelper(object):
    """
    All actions from selenium that are common.
    """

    @staticmethod
    def wait_till_element_clickable(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout, ignored_exceptions=[StaleElementReferenceException])
        try:
            element = wait.until(ec.element_to_be_clickable(locator))
            return element
        except (NoSuchElementException, TimeoutException) as err:
            raise Exception("Element isn't clickable") from err

    @staticmethod
    def wait_till_element_is_displayed(driver, locator, timeout=5):
        """
        :return: True if element IS displayed
        """
        wait = WebDriverWait(driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @staticmethod
    def scroll_to_element(driver, web_element):
        """
        Scroll to the exact element
        :param web_element: web element (e.g. driver.find_element_by_xpath("//div")
        :param driver: webdriver
        """
        driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)

    @staticmethod
    def create_screen_shot(driver, test_name):
        current_date = "_" + (datetime.now().strftime("%Y_%m_%d_%H-%M"))
        save_path = os.path.join(project_path, "screenshots")

        # Create directory for storing screenshots if not exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        driver.save_screenshot(os.path.join(save_path, test_name + current_date + ".png"))

    @staticmethod
    def wait_till_element_text_is_displayed(driver, locator, text, timeout=5):
        """
        :return: True if element text IS displayed
        """
        wait = WebDriverWait(driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            wait.until(ec.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False

    @staticmethod
    def wait_till_all_elements_located(driver, locator, timeout=10):
        """
        :return: True if elements located
        """
        wait = WebDriverWait(driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            return wait.until(ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            return False

    @staticmethod
    def wait_till_element_disappear(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout, ignored_exceptions=[StaleElementReferenceException])
        try:
            wait.until_not(ec.presence_of_element_located(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def wait_till_element_appears(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout, ignored_exceptions=[StaleElementReferenceException])
        try:
            wait.until(ec.presence_of_element_located(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def return_element(driver, locator, timeout=5):
        if UiHelper.wait_till_element_appears(driver, locator, timeout=timeout):
            element = driver.find_element(*locator)
            return element
        raise Exception("Element is missing on the page")

    @staticmethod
    def return_element_attribute(driver, locator, attribute, timeout=5):
        if UiHelper.wait_till_element_appears(driver, locator, timeout=timeout):
            element = driver.find_element(*locator)
            return element.get_attribute(attribute)
        raise Exception("Element is missing on the page")

    @staticmethod
    def click(driver, locator, timeout=5):
        if UiHelper.wait_till_element_appears(driver, locator, timeout=timeout):
            element = UiHelper.return_element(driver, locator)
            UiHelper.scroll_to_element(driver, element)
            element = UiHelper.wait_till_element_clickable(driver, locator)
            element.click()
        else:
            raise Exception("Element is missing on the page")

