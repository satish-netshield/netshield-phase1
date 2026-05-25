import platform
import socket

print("===NetShield System Info ===")
print("Hostname:", socket.gethostname())
print("OS:", platform.system())
print("Release:", platform.release())

with open("../logs/system_info.log", "w") as f:
    f.write("Hostname: " + socket.gethostname() + "\n")
    f.write("OS: " + platform.system() + "\n")
    f.write("Release: " + platform.release() + "\n")

print("Log saved to logs/system_info.log")
