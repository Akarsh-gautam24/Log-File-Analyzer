import re
from collections import defaultdict

log_file = "sample_logs.txt"
suspicious_ips = defaultdict(int)
output_file = "detected_ips.txt"

with open(log_file, "r") as file:
    for line in file:
        match = re.search(r'(\d+\.\d+\.\d+\.\d+).*POST /login.*401', line)  # Fixed regex
        if match:
            ip = match.group(1)
            suspicious_ips[ip] += 1

with open(output_file, "w") as out:
    for ip, count in suspicious_ips.items():
        if count >= 3:
            print(f"Suspicious IP found: {ip} - {count} failed login attempts")  # Fixed print
            out.write(f"{ip} - {count} failed login attempts\n")

print("Log analysis complete. Results saved to 'detected_ips.txt'")  # Proper message
