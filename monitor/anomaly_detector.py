def detect_anomaly(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if "ERROR" in line or "Exception" in line:
            return line
    return None
