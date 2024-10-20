from enums.field_labels import FieldLabels
from enums.report_tab_labels import ReportTab
from enums.sections_labels import SectionsLabels
from pages.validation_page import ValidationPage
from pages.validation_result_page import ValidationResultPage
from utils.tools.verify import Verify
from utils.base_test import BaseTest


class TestPdfValidation(BaseTest):
    """
    Perform test for validation of pdf file
    """

    def test_pdf_validation(self):
        pdf_file = ["test-valid-signature-signed-LTA.pdf"]

        # Signature values
        signature_qualification = ["QESig"]
        signature_qualification_details = ["The organization name is missing in the trusted certificate!"]
        signature_format = ["PAdES-BASELINE-LTA"]
        signature_indication = ["TOTAL_PASSED"]
        signature_certificate_chain = ["Noé Colbach (Signature)", "Citizen CA", "Belgium Root CA4"]
        signature_on_claimed_time = ["2021-10-13 08:50:34 (UTC)"]
        signature_best_signature_time = ["2021-10-13 08:50:40 (UTC)"]
        signature_position = ["1 out of 1"]
        signature_scope = ["Partial PDF (PARTIAL)", "The document ByteRange : [0, 31517, 69407, 773]"]

        # Timestamp 1 values
        timestamp_1 = "Timestamp TIMESTAMP_Ministero-della-Difesa-Time-Stamp-Unit-eIDAS-202109140827_20211013-0850"
        timestamp_1_qualification = ["QTSA"]
        timestamp_1_indication = ["PASSED"]
        timestamp_1_certificate_chain = ["Ministero della Difesa - Time Stamp Unit eIDAS 202109140827",
                                         "Ministero della Difesa - Time Stamp Authority eIDAS"]
        timestamp_1_production_time = ["2021-10-13 08:50:40 (UTC)"]

        # Timestamp 2 values
        timestamp_2 = "Timestamp TIMESTAMP_SK-TIMESTAMPING-AUTHORITY-2021_20211014-0849"
        timestamp_2_qualification = ["QTSA"]
        timestamp_2_indication = ["PASSED"]
        timestamp_2_certificate_chain = ["SK TIMESTAMPING AUTHORITY 2021",
                                         "EE Certification Centre Root CA"]
        timestamp_2_production_time = ["2021-10-14 08:49:54 (UTC)"]
        timestamp_2_timestamp_scope = ["Full PDF (FULL)",
                                       "The document ByteRange : [0, 95717, 133607, 774]"]

        # Document information values
        document_information_pdf_profile = ["PDF/A-1B"]
        document_information_signatures_status = ["1 valid signatures, out of 1"]
        document_information_document_name = pdf_file

        validation_page = ValidationPage(self.driver)
        Verify.true(validation_page.is_validation_page_displayed(),
                    "Validation Page is missing")

        validation_page.set_signed_file(pdf_file)
        Verify.true(validation_page.is_signed_file_uploaded(pdf_file),
                    "File isn't uploaded")

        validation_page.submit_validation()

        validation_result_page = ValidationResultPage(self.driver)
        Verify.true(validation_result_page.is_validation_result_page_displayed(),
                    "Validation Result Page is missing")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Signature.value,
                                                              FieldLabels.Qualification.value,
                                                              signature_qualification),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Signature.value,
                                                              FieldLabels.Qualification_details.value,
                                                              signature_qualification_details),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Signature.value,
                                                              FieldLabels.Signature_format.value,
                                                              signature_format),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Signature.value,
                                                              FieldLabels.Indication.value,
                                                              signature_indication),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Signature.value,
                                                              FieldLabels.Certificate_chain.value,
                                                              signature_certificate_chain),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Signature.value,
                                                              FieldLabels.On_claimed_time.value,
                                                              signature_on_claimed_time),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Signature.value,
                                                              FieldLabels.Best_signature_time.value,
                                                              signature_best_signature_time),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Signature.value,
                                                              FieldLabels.Signature_position.value,
                                                              signature_position),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Signature.value,
                                                              FieldLabels.Signature_scope.value,
                                                              signature_scope),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              timestamp_2,
                                                              FieldLabels.Qualification.value,
                                                              timestamp_2_qualification),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              timestamp_2,
                                                              FieldLabels.Indication.value,
                                                              timestamp_2_indication),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              timestamp_2,
                                                              FieldLabels.Certificate_chain.value,
                                                              timestamp_2_certificate_chain),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              timestamp_2,
                                                              FieldLabels.Production_time.value,
                                                              timestamp_2_production_time),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              timestamp_2,
                                                              FieldLabels.Timestamp_scope.value,
                                                              timestamp_2_timestamp_scope),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              timestamp_1,
                                                              FieldLabels.Qualification.value,
                                                              timestamp_1_qualification),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              timestamp_1,
                                                              FieldLabels.Indication.value,
                                                              timestamp_1_indication),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              timestamp_1,
                                                              FieldLabels.Certificate_chain.value,
                                                              timestamp_1_certificate_chain),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              timestamp_1,
                                                              FieldLabels.Production_time.value,
                                                              timestamp_1_production_time),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Document_Information.value,
                                                              FieldLabels.PDF_A_Profile.value,
                                                              document_information_pdf_profile),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Document_Information.value,
                                                              FieldLabels.Signatures_status.value,
                                                              document_information_signatures_status),
                    "Value is missing on result page")

        Verify.true(validation_result_page.verify_report_data(ReportTab.Simple_Report.value,
                                                              SectionsLabels.Document_Information.value,
                                                              FieldLabels.Document_name.value,
                                                              document_information_document_name),
                    "Value is missing on result page")







