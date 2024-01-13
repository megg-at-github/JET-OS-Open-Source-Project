import tkinter as tk
import psutil
import socket
import datetime


import jet_editor



# Function to get IP address
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Function to update the GUI labels
def update_labels():
    # Battery status
    battery_status = psutil.sensors_battery()
    if battery_status is not None:
        plug_status = "Plugged in" if battery_status.power_plugged else "Not plugged in"
        battery_percent = battery_status.percent
        battery_label.config(text=f"Battery: {battery_percent}% ({plug_status})")

    # Time and date
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    time_label.config(text=f"Time: {current_time}")
    date_label.config(text=f"Date: {current_date}")

    # IP address
    ip_address = get_ip_address()
    ip_label.config(text=f"IP Address: {ip_address}")

    # CPU and RAM usage
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    ram_label.config(text=f"RAM Usage: {ram_usage}%")

    # Update labels every 1 second
    root.after(1000, update_labels)

# Create the GUI window
root = tk.Tk()
root.title("JET OS")
root.geometry("400x300")

# Create labels for battery, time, date, IP address, MAC address, CPU and RAM usage
battery_label = tk.Label(root, font=("Arial", 14))
battery_label.pack(pady=10)

time_label = tk.Label(root, font=("Arial", 14))
time_label.pack()

date_label = tk.Label(root, font=("Arial", 14))
date_label.pack()

ip_label = tk.Label(root, font=("Arial", 14))
ip_label.pack()

mac_label = tk.Label(root, font=("Arial", 14))
mac_label.pack()

cpu_label = tk.Label(root, font=("Arial", 14))
cpu_label.pack()

ram_label = tk.Label(root, font=("Arial", 14))
ram_label.pack()

# Update the labels
update_labels()

def jet_editor():
    import subprocess
import tkinter as tk
from tkinter import filedialog
import pdb

root = tk.Tk()
root.title("JET Editor")

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".wmf" or ".html" or ".css" or ".pdf" or ".txt" or ".sh" or ".bash" or ".py")
    if file is None:
        return
    text = str(text_editor.get(1.0, tk.END))
    file.write(text)
    file.close()

def html_file():
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.END, "<!DOCTYPE html>\n<html>\n<head>\n<title>My HTML File</title>\n</head>\n<body>\n\n</body>\n</html>")

def css_file():
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.END, "/* Add your CSS code here */")

def new_file():
    text_editor.delete(1.0, tk.END)

def available_extensions():
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.END, ".wmf, .html, .css, .pdf(still in developement), .txt, .sh, .bash(same as .sh)")

def open_file():
    file = filedialog.askopenfile(mode='r')
    if file is None:
        return
    text = file.read()
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.END, text)
    file.close()

text_editor = tk.Text(root)
text_editor.pack()

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

open_button = tk.Button(root, text="Open", command=open_file)
open_button.pack()

new_button = tk.Button(root, text="New", command=new_file)
new_button.pack()

html_button = tk.Button(root, text="HTML DOC", command=html_file)
html_button.pack()

css_button = tk.Button(root, text="CSS FILE", command=css_file)
css_button.pack()

extensions_button = tk.Button(root, text="Available Extensions", command=available_extensions)
extensions_button.pack()

import tkinter as tk

def encrypt_text():
    text = text_editor.get("1.0", "end-1c")
    encrypted_text = "".join([str(ord(char)) for char in text])
    text_editor.delete("1.0", "end")
    text_editor.insert("1.0", encrypted_text)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

root.mainloop()


def jet_editor_button():
    jet_editor_window = tk.Toplevel(root)
    jet_editor_window.title("JET Editor")
    jet_editor_window.geometry("500x300")

jet_editor_button = tk.Button(root, text="JET Editor", command=jet_editor_button)
jet_editor_button.pack()

# Run the GUI
root.mainloop()











    



