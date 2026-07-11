#!/usr/bin/env python3
import psutil

# Check CPU load across all cores
cpu_pct = psutil.cpu_percent(interval=1)

# Check physical RAM metrics
memory = psutil.virtual_memory()

print(f"System Health Baseline:")
print(f"  - CPU Usage: {cpu_pct}%")
print(f"  - RAM Available: {memory.available / (1024**2):.2f} MB ({memory.percent}% Used)")

if cpu_pct > 90 or memory.percent > 90:
    print("🚨 Alert: System under severe resource pressure.")
