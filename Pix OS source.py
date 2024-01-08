print('Welcome to Pix OS')

running = input('Do you want to run this OS? ')
if running != 'yes': 
    quit()
    
print('Ok, running OS :)') 

running = input('Enter Password ')
if running !='PLACEHOLDER.PASSWORD':
    quit()

import bcrypt

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_password.decode("utf-8")

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


import datetime
from battery_status import get_battery_info

from pc_info import get_pc_info

from cpu_gpu import get_cpu_name
from cpu_gpu import get_gpu_name

import system_monitor

from ip_address_viewer import get_ip_address

from mac_address_viewer import get_mac_address

print(datetime.datetime.now())

print(get_pc_info())

print(get_cpu_name())
print(get_gpu_name())

print(system_monitor.get_cpu_usage())

print(system_monitor.get_memory_usage())

print(get_ip_address())

print(get_mac_address())

# Within your program's logic, where you want to display the battery status:
battery_info = get_battery_info()
print(battery_info)  # Or use the information as needed in your program

running = input("Type and Enter 'quit()'for quitting the program ")











    



