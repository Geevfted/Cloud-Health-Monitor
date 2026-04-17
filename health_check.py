import time
import random
import json
import smtplib
from email.message import EmailMessage

# --- CONFIGURATION ---
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"  # The 16-char code
RECEIVER_EMAIL = "your-email@gmail.com"

def send_email_alert(log_entry):
    msg = EmailMessage()
    msg.set_content(f"System Failure Detected!\n\nDetails:\n{json.dumps(log_entry, indent=4)}")
    msg['Subject'] = f"ALERT: System Status {log_entry['status']}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        # Connect to Gmail's server (SMTP)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
            print("Email alert sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def run_check():
    is_healthy = random.random() > 0.2
    status = 200 if is_healthy else 500
    
    log_entry = {
        "status": status,
        "message": "Healthy" if is_healthy else "CRITICAL FAILURE",
        "timestamp": time.ctime()
    }

    print(f"Check Result: {status}")
    
    if status == 500:
        print("Triggering Email Alert...")
        send_email_alert(log_entry)

if __name__ == "__main__":
    run_check()
