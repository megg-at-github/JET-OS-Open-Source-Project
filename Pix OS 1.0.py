print('Welcome to Pix OS ')

import password 
# Minimum length
min_length = 10
required_classes = {
}

notif = input("Enter Password")

if not password.check(login_key, min_length, required_classes):
    print("Login key does not meet complexity requirements.")
    print("Please ensure your password has:")
    print(f"- At least {min_length} characters")
    print("- One uppercase letter")
    print("- One lowercase letter")
    print("- One number")
    print("- One symbol")
    quit()

import bcrypt

salt = bcrypt.gensalt()

password = "[PLACEHOLDER_PASSWORD]".encode('utf-8')
hashed_password = bcrypt.hashpw(password, salt)

if bcrypt.checkpw(password, hashed_password):
    print("Password matched")
else:
    print("Password did not match.")

if input == "[PLACEHOLDER_PASSWORD]":
    print('Access Granted')
else:
    print(f"Access Denied")

import datetime
now = datetime.datetime.now()

formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Example format: 2023-12-27 11:42:00

print("Current time:", formatted_time)

if input == "time":
    print("Current time:", formatted_time)
else: quit()

import psutil

battery = psutil.sensors_battery()
percent = battery.percent
print("Battery charge:", percent, "%")

if input == "battery status":
    print("Battery charge:", percent, "%")
else: quit() 







