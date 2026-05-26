import sqlite3
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "netshield.db")

print("=== NetShield Attack Threshold Detector ===")

# Connect to database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Get ALERT messages
cursor.execute("SELECT message FROM incidents WHERE level='ALERT'")
rows = cursor.fetchall()

ip_count = {}

# Extract IPs
for row in rows:
    message = row[0]

    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', message)

    for ip in ips:
        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1

# Detect repeated attacks
threshold = 3

print("\nAttack Analysis Report:\n")

for ip, count in ip_count.items():

    if count >= threshold:
        print(f"[HIGH RISK] {ip} detected {count} times")
        print("Possible brute force or repeated attack detected\n")

    else:
        print(f"[LOW RISK] {ip} detected {count} time(s)\n")

conn.close()
