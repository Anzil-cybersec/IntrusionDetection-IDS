# brute_force_detection.py

import time
from collections import defaultdict

def detect_brute_force(ip, timestamp, failed_attempts, max_attempts=5, time_window=60):
    """
    Detects Brute Force attacks based on failed login attempts from the same IP.
    :param ip: The IP address to check.
    :param timestamp: The current timestamp of the failed attempt.
    :param failed_attempts: Dictionary tracking failed attempts for each IP.
    :param max_attempts: Maximum allowed failed attempts within time_window before flagging as brute force.
    :param time_window: Time window (in seconds) to check for failed attempts.
    :return: Boolean indicating whether a Brute Force attack was detected.
    """
    # Clean up failed attempts older than the time window
    failed_attempts[ip] = [t for t in failed_attempts[ip] if t > timestamp - time_window]
    
    # Add the new failed attempt
    failed_attempts[ip].append(timestamp)

    if len(failed_attempts[ip]) > max_attempts:
        print(f"Brute force detected from {ip}")
        return True  # Brute Force detected
    return False
