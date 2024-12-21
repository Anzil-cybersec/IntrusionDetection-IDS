
# main.py

import time
from ddos_detection import detect_ddos
from brute_force_detection import detect_brute_force
from sql_injection_detection import detect_sql_injection
from collections import defaultdict

def main():
    # Example of DDoS detection with fake packet data
    print("\nDetecting DDoS attack...")
    packet_data = [{'src_ip': '192.168.1.1'}, {'src_ip': '192.168.1.1'}, {'src_ip': '192.168.1.2'}]
    detect_ddos(packet_data)

    # Example of Brute Force detection
    print("\nDetecting Brute Force attack...")
    failed_attempts = defaultdict(list)  # Track failed login attempts per IP
    ip = '192.168.1.1'
    timestamp = time.time()
    detect_brute_force(ip, timestamp, failed_attempts)

    # Example of SQL Injection detection
    print("\nDetecting SQL Injection attack...")
    query = "SELECT * FROM users WHERE username='admin' --"
    detect_sql_injection(query)

if __name__ == "__main__":
    main()
