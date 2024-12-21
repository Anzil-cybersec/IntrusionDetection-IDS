# sql_injection_detection.py

import re

def detect_sql_injection(query):
    """
    Detects potential SQL Injection attempts in a query.
    :param query: The SQL query string.
    :return: Boolean indicating whether SQL injection patterns were found.
    """
    # List of common SQL injection patterns
    patterns = [r"(?i)\b(select|insert|update|drop|delete|union|--|\b'or\b)\b"]
    
    for pattern in patterns:
        if re.search(pattern, query):
            print("SQL Injection detected!")
            return True  # SQL Injection detected
    return False
