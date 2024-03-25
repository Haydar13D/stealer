import subprocess
import os
import sys

# Create a file
password_file = open('password.txt', "w")
password_file.write("Nyoh password mu:\n\n")
password_file.close()

# List
wifi_files = []
wifi_name = []
wifi_password = []

# Use Python to execute command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"],
                         capture_output=True).stdout.decode()

# Grab the current directory
path = os.getcwd()

# Iterate through Wi-Fi files
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith("xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, "r") as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = stripped[:-7]
                        wifi_name.append(back)
                    if 'KeyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = stripped[:-14]
                        wifi_password.append(back)

# Write Wi-Fi information to the password file
with open("password.txt", "a") as output_file:
    for x, y in zip(wifi_name, wifi_password):
        output_file.write(f"SSID: {x}\nPassword: {y}\n\n")
