from ocr_parser import extract_invoice_data
from finance_logic import analyze_finances
from mailer import send_report

def main():
    print("🔹 AI CFO MVP Started")

    # Sample input (you can later connect this to uploaded files)
    invoice_path = "sample_invoice.jpg"
    user_email = "demo@example.com"

    # Step 1: OCR extraction
    data = extract_invoice_data(invoice_path)
    print("✅ OCR Data Extracted:", data)

    # Step 2: Analyze finances
    report = analyze_finances(data)
    print("💡 Financial Analysis Done:", report)

    # Step 3: Email report
    send_report(user_email, report)
    print("📧 Report sent to user!")

if __name__ == "__main__":
    main()

