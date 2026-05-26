from collections import Counter
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "logs", "incidents.log")

print("=== NetShield Incident Report ===\n")

try:
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    levels = []

    for line in lines:
        if "[INFO]" in line:
            levels.append("INFO")
        elif "[WARN]" in line:
            levels.append("WARN")
        elif "[ALERT]" in line:
            levels.append("ALERT")

    count = Counter(levels)

    print("Total Incidents:", len(lines))
    print("INFO:", count.get("INFO", 0))
    print("WARN:", count.get("WARN", 0))
    print("ALERT:", count.get("ALERT", 0))

except FileNotFoundError:
    print("No incident log found. Run simulator first.")
