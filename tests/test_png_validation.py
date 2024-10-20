from pages.validation_page import ValidationPage
from pages.validation_result_page import ValidationResultPage
from utils.tools.verify import Verify
from utils.base_test import BaseTest


class TestPngValidation(BaseTest):
    """
    Perform test for validation of png file
    """

    def test_png_validation(self):
        png_file = ["test_1.png"]

        validation_page = ValidationPage(self.driver)
        Verify.true(validation_page.is_validation_page_displayed(),
                    "Validation Page is missing")

        validation_page.set_signed_file(png_file)
        Verify.true(validation_page.is_signed_file_uploaded(png_file),
                    "File isn't uploaded")

        validation_page.submit_validation()
        validation_result_page = ValidationResultPage(self.driver)
        Verify.true(validation_result_page.is_validation_error_heading_displayed(),
                    "Validation error is missing")

        Verify.true(validation_result_page.is_validation_error_message_displayed(),
                    "Validation error is missing")

