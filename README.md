# IntrusionDetection-IDS
A Python-based Intrusion Detection System (IDS) designed to detect common network attacks such as DDoS, Brute Force, SQL Injection, and more. Modular and easy to extend for additional attack types

- **DDoS (Distributed Denial of Service)**
- **Brute Force**
- **SQL Injection**

### Features:
- **DDoS Detection**: Detects excessive requests from the same IP address within a short time.
- **Brute Force Detection**: Detects failed login attempts exceeding a threshold for a given IP address.
- **SQL Injection Detection**: Detects potential SQL injection patterns in SQL queries.

### How to Run:
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the IDS with `python main.py`.

### Notes:
- The detection methods are simple and use basic heuristics for identifying attacks.
- The code is designed to be modular, so additional attack detection methods can be easily added.

