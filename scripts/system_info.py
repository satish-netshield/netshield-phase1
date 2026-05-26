import os
import socket
import platform

# Get project root safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR, "logs", "system_info.log")

print("===NetShield System Info ===")
print("Hostname:", socket.gethostname())
print("OS:", platform.system())
print("Release:", platform.release())

with open(LOG_PATH, "w") as f:
    f.write("Hostname: " + socket.gethostname() + "\n")
    f.write("OS: " + platform.system() + "\n")
    f.write("Release: " + platform.release() + "\n")

print("Log saved to logs/system_info.log")
