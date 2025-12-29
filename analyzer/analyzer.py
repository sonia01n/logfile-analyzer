from collections import Counter, defaultdict

def analyze_logs(log_entries):
    error_messages = Counter()
    error_by_hour = defaultdict(int)

    for entry in log_entries:
        if entry["level"] == "ERROR":
            error_messages[entry["message"]] += 1
            error_by_hour[entry["timestamp"].hour] += 1

    return error_messages, error_by_hour
