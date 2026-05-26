import sqlite3
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "netshield.db")

print("=== NetShield Suspicious IP Tracker ===")

# Connect to database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Get ALERT messages
cursor.execute("SELECT message FROM incidents WHERE level='ALERT'")
rows = cursor.fetchall()

ip_count = {}

# Find IP addresses
for row in rows:
    message = row[0]

    # Regex to find IP addresses
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', message)

    for ip in ips:
        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1

# Print results
if ip_count:
    print("\nSuspicious IP Summary:")
    for ip, count in ip_count.items():
        print(f"{ip} detected {count} time(s)")
else:
    print("No suspicious IPs found.")

conn.close()
