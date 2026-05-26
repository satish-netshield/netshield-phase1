import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "netshield.db")

print("=== NetShield SQL Log Analysis ===")

# Connect to database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Total incidents
cursor.execute("SELECT COUNT(*) FROM incidents")
total = cursor.fetchone()[0]

# Count INFO logs
cursor.execute("SELECT COUNT(*) FROM incidents WHERE level='INFO'")
info_count = cursor.fetchone()[0]

# Count WARN logs
cursor.execute("SELECT COUNT(*) FROM incidents WHERE level='WARN'")
warn_count = cursor.fetchone()[0]

# Count ALERT logs
cursor.execute("SELECT COUNT(*) FROM incidents WHERE level='ALERT'")
alert_count = cursor.fetchone()[0]

# Print report
print(f"Total Incidents: {total}")
print(f"INFO Events: {info_count}")
print(f"WARN Events: {warn_count}")
print(f"ALERT Events: {alert_count}")

conn.close()
