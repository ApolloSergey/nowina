from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helpers.ui_helper import UiHelper
from utils.helpers.common_actions import CommonActions
from utils.tools.logs import log


class ValidationResultPage(BasePage):

    VALIDATION_RESULT_PAGE_HEADER = (By.XPATH, "//h1[contains(text(),'Validation results')]")
    VALIDATION_ERROR_PAGE_HEADER = (By.XPATH, "//h1[contains(text(),'Bad Request')]")
    VALIDATION_ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-danger') and "
                                          "span[contains(., 'Document format not recognized/handled')]]")
    SECTION_HEADER_XPATH = ("//div[@id='simple-report']//div[contains(@class, 'card-header')]"
                            "[contains(normalize-space(), '{}')]")
    SECTION_FIELD_NAME_VALUE_XPATH = "//dl[dt[contains(text(), '{}')] and dd[contains(., '{}')]]"

    def is_validation_result_page_displayed(self):
        log.info("Verify Validation Result page is displayed")
        return UiHelper.wait_till_element_is_displayed(self.driver, self.VALIDATION_RESULT_PAGE_HEADER)

    def is_validation_error_heading_displayed(self):
        log.info("Verify error heading on Validation Result page")
        return UiHelper.wait_till_element_is_displayed(self.driver, self.VALIDATION_ERROR_PAGE_HEADER)

    def is_validation_error_message_displayed(self):
        log.info("Verify error message on Validation Result page")
        return UiHelper.wait_till_element_is_displayed(self.driver, self.VALIDATION_ERROR_MESSAGE)

    def expand_report_section(self, section_name):
        if "Timestamp" in section_name:
            section_name = "Timestamps"
        section_xpath = (By.XPATH, self.SECTION_HEADER_XPATH.format(section_name))
        element = UiHelper.return_element(self.driver, section_xpath)
        UiHelper.scroll_to_element(self.driver, element)
        try:
            extended_status = CommonActions.strtobool(
                UiHelper.return_element_attribute(self.driver, section_xpath, "aria-expanded"))
        except Exception:
            extended_status = True
        if not extended_status:
            UiHelper.click(self.driver, section_xpath)

    def select_report_tab(self, report_tab):
        pass

    def verify_report_data(self, report_tab, section_name, field_name, field_value):
        log.info("Verify {} tab, {} section on Validation Result page".
                 format(report_tab, section_name))
        self.select_report_tab(report_tab)
        self.expand_report_section(section_name)
        parent_root_xpath = self.SECTION_HEADER_XPATH.format(section_name) + "/parent::div"
        root_element = self.driver.find_element(By.XPATH, parent_root_xpath)
        if len(field_value) == 1:
            element_xpath = self.SECTION_FIELD_NAME_VALUE_XPATH.format(field_name, field_value[0])
            return UiHelper.wait_till_element_appears(root_element, (By.XPATH, element_xpath))
        status = []
        for value in field_value:
            element_xpath = self.SECTION_FIELD_NAME_VALUE_XPATH.format(field_name, value)
            status.append(UiHelper.wait_till_element_appears(root_element, (By.XPATH, element_xpath)))
        return all(status)
