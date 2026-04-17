import time
import random
import json
import boto3

LOCALSTACK_URL = "http://localhost:4566"
GROUP_NAME = "/cloud-monitor/health-checks"
STREAM_NAME = "heartbeat-monitor"

def send_log(client, message, status):
    # AWS requires timestamp in milliseconds
    timestamp = int(round(time.time() * 1000))
    
    log_event = {
        'timestamp': timestamp,
        'message': json.dumps({
            "status": status,
            "message": message,
            "system": "Cloud-Monitor-01"
        })
    }
    
    client.put_log_events(
        logGroupName=GROUP_NAME,
        logStreamName=STREAM_NAME,
        logEvents=[log_event]
    )

if __name__ == "__main__":
    # Initialize the bridge
    client = boto3.client("logs", 
                          endpoint_url=LOCALSTACK_URL, 
                          region_name="us-east-1",
                          aws_access_key_id="test", 
                          aws_secret_access_key="test")
    
    # Run a health check and send it to the "Cloud"
    is_healthy = random.random() > 0.2
    msg = "System is Healthy" if is_healthy else "System is Unhealthy"
    stat = 200 if is_healthy else 500
    
    print(f"Attempting to send log: {msg}...")
    send_log(client, msg, stat)
    print("Log sent to LocalStack CloudWatch!")
