Log File Analyzer for Intrusion Detection

This is a simple Python-based project that analyzes server log files to detect brute-force login attempts. It simulates how SOC analysts investigate logs for signs of unauthorized access using pattern detection.

Features:
- Parses Apache-style access logs
- Detects multiple failed login attempts by the same IP address
- Flags suspicious IPs based on HTTP 401 status code patterns
- Outputs suspicious activity to a 'detected_ips.txt' report

Tools Used:
- Python 3.x
- Built-in re (Regular Expressions)
- defaultdict from collections
- Kali Linux

Sample Log Pattern:
192.168.1.2 - - [19/Jun/2025:10:00:02] "POST /login HTTP/1.1" 401 562

The script flags IPs with 3 or more failed login attempts.

How to Run:
1. Place your log file as 'sample_logs.txt' in the project folder
2. Run the script using: python3 log_analyzer.py
3. Check 'detected_ips.txt' for suspicious IPs

Files Included:
- log_analyzer.py – Main Python script
- sample_logs.txt – Sample Apache-style log file
- detected_ips.txt – Output file with flagged IPs
- Log_Analyzer_Report.pdf – Project documentation

Created By:
Akarsh Gautam (GitHub: https://github.com/Akarsh-gautam24)

For Educational Use Only:
This tool is designed for learning purposes and SOC training simulations only.