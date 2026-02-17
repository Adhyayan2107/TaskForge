import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        print("Connecting to SMTP...")

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            print("Logging in...")
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            print("Sending email...")
            server.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print("ERROR:", e)