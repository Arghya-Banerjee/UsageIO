import psutil

print(
    "CPU Temp: ", psutil.cpu_percent(interval=0.1), "%",
)