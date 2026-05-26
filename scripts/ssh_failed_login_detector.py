import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR, "logs", "auth.log")

print("=== NetShield SSH Failed Login Detector ===")

failed_attempts = {}

# Open auth log
with open(LOG_PATH, "r") as file:

    for line in file:

        # Look for failed password attempts
        if "Failed password" in line:

            # Extract IP address
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)

            if ip_match:

                ip = ip_match.group(1)

                if ip in failed_attempts:
                    failed_attempts[ip] += 1
                else:
                    failed_attempts[ip] = 1

# Print report
print("\nFailed Login Summary:\n")

for ip, count in failed_attempts.items():

    if count >= 3:
        print(f"[HIGH RISK] {ip} failed {count} login attempts")

    else:
        print(f"[MEDIUM RISK] {ip} failed {count} login attempt(s)")
