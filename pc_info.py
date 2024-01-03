import platform
import psutil

def get_pc_info():
    info = {
        "Operating System": platform.system() + " " + platform.release(),
        "CPU": platform.processor(),
        "Memory Usage": f"{psutil.virtual_memory().percent:.2f}%",
        "Disk Usage": f"{psutil.disk_usage('/').percent:.2f}%",
    }
    return info
