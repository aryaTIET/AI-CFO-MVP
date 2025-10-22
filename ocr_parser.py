import pytesseract
from PIL import Image
import re

def extract_invoice_data(invoice_path):
    """Extracts key data from an invoice image."""
    img = Image.open(invoice_path)
    text = pytesseract.image_to_string(img)

    # Extract data with regex (simple version)
    total = re.findall(r"Total\s*[:\-]?\s*(\d+[.,]?\d*)", text, re.IGNORECASE)
    vendor = re.findall(r"(?:From|Vendor|Company)[:\-]?\s*(.+)", text)
    date = re.findall(r"(\d{2,4}[-/]\d{2,4}[-/]\d{2,4})", text)

    return {
        "vendor": vendor[0] if vendor else "Unknown Vendor",
        "date": date[0] if date else "Unknown Date",
        "total": float(total[0]) if total else 0.0
    }

