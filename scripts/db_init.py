import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "netshield.db")

print("=== NetShield DB Initialization ===")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    level TEXT,
    message TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully at:", DB_PATH)
