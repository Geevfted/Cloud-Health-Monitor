import time
import random
import json

def run_health_check():
    # 80% success rate
    is_healthy = random.random() > 0.2
    status_code = 200 if is_healthy else 500
    level = "INFO" if is_healthy else "ERROR"
    
    # This dictionary is what we will eventually send to CloudWatch
    log_entry = {
        "timestamp": time.ctime(),
        "status": status_code,
        "message": "System is Healthy" if is_healthy else "System is Unhealthy",
        "level": level
    }
    
    # Convert dictionary to a JSON string
    print(json.dumps(log_entry))

if __name__ == "__main__":
    for i in range(10):
        run_health_check()
        time.sleep(1)
