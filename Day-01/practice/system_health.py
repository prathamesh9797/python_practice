
#Takes threshold values (CPU, disk, memory) from user input
#Also fetches system metrics using a Python library (example: psutil)
#Compares metrics against thresholds
#Prints the result to the terminal



import psutil
def check_system():
    threshold_cpu_value = float(input("enter cpu value"))
    threshold_disk_value = float(input("enter disk value"))
    threshold_memory_value = float(input("enter memory value"))
    
    current_cpu = psutil.cpu_percent(interval=1)
    current_disk = psutil.cpu_percent(interval=1)
    current_memory = psutil.cpu_percent(interval=1)
    
    print("current cpu%: ", current_cpu)
    print("current_disk%: ", current_disk)
    print("current_memory%: ", current_memory)
    
    if (
    threshold_cpu_value > current_cpu and
    threshold_disk_value > current_disk and
    threshold_memory_value > current_memory
    ):
        print("system is healthy")
        
    else:
        print("system threshold exceeded")
check_system()