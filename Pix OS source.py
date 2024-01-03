print('Welcome to Pix OS')

running = input('Do you want to run this OS? ')
if running != 'yes': 
    quit()
    
print('Ok, running OS :)') 

running = input('Enter Password ')
if running != 'PLACEHOLDER.PASSWORD':
    quit()

import datetime
from battery_status import get_battery_info

from pc_info import get_pc_info

print(datetime.datetime.now())

print(get_pc_info())

if running != 'time':
    quit()
print(datetime.datetime.now()) 

# Within your program's logic, where you want to display the battery status:
battery_info = get_battery_info()
print(battery_info)  # Or use the information as needed in your program







    



