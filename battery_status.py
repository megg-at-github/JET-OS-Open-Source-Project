import psutil

def get_battery_info():
    """Retrieves and formats battery information."""
    battery = psutil.sensors_battery()
    if battery is None:
        return "No battery detected."
    return f"Battery percentage: {battery.percent}%\nPlugged in: {battery.power_plugged}"

while True:
    user_input = input("Type 'battery' to check battery status, or 'quit' to exit: ")
    if user_input.lower() == "battery":
        print(get_battery_info())
    elif user_input.lower() == "quit":
        break
