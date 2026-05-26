import os
import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "logs", "incidents.log")

def log_incident(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{level}] {message}\n"

    with open(LOG_FILE, "a") as f:
        f.write(entry)

    print(entry.strip())

print("=== NetShield Incident Simulator ===")

# Simulated events
events = [
    ("INFO", "System scan started"),
    ("WARN", "Multiple failed login attempts detected"),
    ("ALERT", "Suspicious IP detected: 192.168.1.100"),
    ("INFO", "Incident response triggered"),
]

for level, msg in events:
    log_incident(level, msg)
    time.sleep(1)

print("Simulation complete. Check logs/incidents.log")
