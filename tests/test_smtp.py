import smtplib
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def test_smtp_connection():
    try:
        # Fetch SMTP configuration from environment variables
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT"))
        smtp_username = os.getenv("SMTP_USERNAME")
        smtp_password = os.getenv("SMTP_PASSWORD")

        # Establish connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade to a secure connection
        server.login(smtp_username, smtp_password)
        print("SMTP connection successful!")
    except Exception as e:
        print(f"SMTP connection failed: {e}")
    finally:
        # Ensure the connection is closed if it was established
        try:
            server.quit()
        except Exception:
            pass  # Ignore errors in closing the connection
