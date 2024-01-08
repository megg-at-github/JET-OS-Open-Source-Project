import platform
import subprocess

def get_cpu_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        return subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"]).strip().decode()
    elif platform.system() == "Linux":
        with open("/proc/cpuinfo", "r") as f:
            for line in f.readlines():
                if "model name" in line:
                    return line.split(":")[1].strip()
    return "Unknown CPU"

def get_gpu_name():
    if platform.system() == "Windows":
        try:
            import WMI
            w = WMI.WMI(namespace="root\\cimv2")
            gpu_info = w.query("SELECT * FROM Win32_VideoController")[0]
            return gpu_info.Name
        except:
            return "Unknown GPU"
    elif platform.system() == "Darwin":
        return subprocess.check_output(["system_profiler", "SPDisplaysDataType"]).strip().split(b"\n")[-1].split(b":")[-1].strip().decode()
    elif platform.system() == "Linux":
        try:
            lspci_out = subprocess.check_output(["lspci", "-v"]).decode()
            return lspci_out.split("\n")[0].split(":")[-1].strip()
        except:
            return "Unknown GPU"
    return "Unknown GPU"

print(f"CPU Name: {get_cpu_name()}")
print(f"GPU Name: {get_gpu_name()}")
