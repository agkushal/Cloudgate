# client/send_event.py
import requests

def send_log(source, event_type, message):
    payload = {
        "source": source,
        "event_type": event_type,
        "message": message
    }
    try:
        response = requests.post("http://localhost:5000/log", json=payload)
        print("Log sent:", response.json())
    except Exception as e:
        print("Error:", e)

# Example
if __name__ == '__main__':
    send_log("sensor_A", "error", "Temperature threshold exceeded")
