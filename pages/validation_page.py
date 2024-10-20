from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helpers.ui_helper import UiHelper
from utils.tools.logs import log
from utils.helpers.common_actions import CommonActions


class ValidationPage(BasePage):

    SIGNED_FILE_INPUT = (By.ID, "signedFile")
    ORIGINAL_FILES_INPUT = (By.ID, "detachedOriginalFiles")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    VALIDATION_PAGE_HEADER = (By.XPATH, "//h1[contains(text(),'Validate a signature')]")

    def is_validation_page_displayed(self):
        log.info("Verify Validation page is displayed")
        return UiHelper.wait_till_element_is_displayed(self.driver, self.VALIDATION_PAGE_HEADER)

    def is_signed_file_uploaded(self, file_name):
        name = UiHelper.return_element_attribute(self.driver, self.SIGNED_FILE_INPUT, "value")
        return file_name[0] in name

    def set_signed_file(self, file_name):
        file_path = CommonActions.get_path_to_file_names(file_name)
        UiHelper.return_element(self.driver, self.SIGNED_FILE_INPUT).send_keys(file_path)

    def set_original_files(self, file_name):
        file_path = CommonActions.get_path_to_file_names(file_name)
        UiHelper.return_element(self.driver, self.ORIGINAL_FILES_INPUT).send_keys(file_path)

    def submit_validation(self):
        UiHelper.click(self.driver, self.SUBMIT_BUTTON)
