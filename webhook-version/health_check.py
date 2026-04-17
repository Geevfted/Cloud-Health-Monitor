import time
import random
import json
import boto3
import requests  # To send the Webhook

LOCALSTACK_URL = "http://localhost:4566"
WEBHOOK_URL = "https://hook.us2.make.com/6qg8v66lcz9yaymnd14xkcu60v8xxmhe" # Replace this with your automation URL like make.com

def trigger_alert(log_data):
    if WEBHOOK_URL == "https://hook.us2.make.com/6qg8v66lcz9yaymnd14xkcu60v8xxmhe":
        print("Alert skipped: No Webhook URL provided.")
        return
    
    # Send the "Failure" data to your automation
    response = requests.post(WEBHOOK_URL, json=log_data)
    if response.status_code == 200:
        print("Successfully sent alert to Make/Zapier!")

def run_check():
    is_healthy = random.random() > 0.2
    status = 200 if is_healthy else 500
    
    log_entry = {
        "status": status,
        "message": "System is Healthy" if is_healthy else "CRITICAL: System Unhealthy",
        "timestamp": time.ctime()
    }

    # Always log to LocalStack CloudWatch
    print(f"Logging to CloudWatch: {log_entry['status']}")
    
    # ONLY trigger the automation if it's a failure (500)
    if status == 500:
        print("!!! FAILURE DETECTED - Triggering Alert !!!")
        trigger_alert(log_entry)

if __name__ == "__main__":
    # We will just run it once to test the trigger
    run_check()
