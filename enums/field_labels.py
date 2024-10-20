from enum import Enum


class FieldLabels(Enum):
    """
    List of Field Labels
    """

    # Validation results page
    Qualification = "Qualification"
    Qualification_details = "Qualification Details"
    Signature_format = "Signature format"
    Indication = "Indication"
    Certificate_chain = "Certificate Chain"
    On_claimed_time = "On claimed time"
    Best_signature_time = "Best signature time"
    Signature_position = "Signature position"
    Signature_scope = "Signature scope"
    Production_time = "Production time"
    Timestamp_scope = "Timestamp scope"
    PDF_A_Profile = "PDF/A Profile"
    Signatures_status = "Signatures status"
    Document_name = "Document name"
