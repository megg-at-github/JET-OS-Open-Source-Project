import os
import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def main():
    print("Monitoring CPU and RAM usage. Press Ctrl+C to exit.")
    try:
        while True:
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()

            print(f"CPU Usage: {cpu_usage:.2f}% | Memory Usage: {memory_usage:.2f}%")
            time.sleep(2)  # Adjust the interval as needed
    except KeyboardInterrupt:
        print("\nMonitoring stopped. Goodbye!")

if __name__ == "__main__":
    main()

