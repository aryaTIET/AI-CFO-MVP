import smtplib
from email.mime.text import MIMEText

def send_report(email, report):
    """Sends a simple text report via Gmail."""
    sender = "yourgmail@gmail.com"
    app_password = "your-app-password"  # Generate from Google Account

    subject = f"Your AI CFO Report — {report['vendor']}"
    body = f"""
    Invoice Report
    ---------------
    Vendor: {report['vendor']}
    Date: {report['date']}
    Total: ₹{report['total']}
    Financial Score: {report['score']}/100
    Insight: {report['insight']}
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, app_password)
        server.sendmail(sender, email, msg.as_string())
    print("✅ Email sent successfully!")

