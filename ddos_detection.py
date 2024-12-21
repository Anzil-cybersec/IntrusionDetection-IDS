# ddos_detection.py

from collections import defaultdict

def detect_ddos(packet_data, threshold=100):
    """
    Detects DDoS attack by counting requests from the same IP within a short time period.
    :param packet_data: List of packets, each packet is a dictionary with 'src_ip'.
    :param threshold: Number of requests from the same IP to flag as a potential DDoS.
    :return: Boolean indicating whether a DDoS attack was detected.
    """
    src_ips = [pkt['src_ip'] for pkt in packet_data]
    ip_counts = defaultdict(int)
    
    for ip in src_ips:
        ip_counts[ip] += 1
        
    for ip, count in ip_counts.items():
        if count > threshold:
            print(f"DDoS Attack detected! {ip} made {count} requests.")
            return True  # DDoS detected
    return False
