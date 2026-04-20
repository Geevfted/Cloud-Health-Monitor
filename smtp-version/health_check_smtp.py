import time
import random
import json
import smtplib
import os
from email.message import EmailMessage

# --- CONFIGURATION ---
# Replace the email below with your actual Gmail/Outlook address
SENDER_EMAIL = "geevfted@gmail.com"
RECEIVER_EMAIL = "jesseadaramoye19@gmail.com"

# This line grabs the password you set in Step 1
SENDER_PASSWORD = os.getenv('EMAIL_PASSWORD')

def send_email_alert(log_entry):
    if not SENDER_PASSWORD:
        print("Error: No password found in environment variables!")
        return

    msg = EmailMessage()
    msg.set_content(f"System Failure Detected!\n\nDetails:\n{json.dumps(log_entry, indent=4)}")
    msg['Subject'] = f"ALERT: System Status {log_entry['status']}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        # We use Gmail's SMTP server as the default
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
            print("Email alert sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def run_check():
    # Simulate a health check (20% chance of failure)
    is_healthy = random.random() > 0.2
    status = 200 if is_healthy else 500
    
    log_entry = {
        "status": status,
        "message": "System Healthy" if is_healthy else "CRITICAL FAILURE",
        "timestamp": time.ctime()
    }

    print(f"Current System Status: {status}")
    
    # Only send email if the status is 500 (Failure)
    if status == 500:
        print("Triggering Email Alert...")
        send_email_alert(log_entry)

if __name__ == "__main__":
    run_check()
