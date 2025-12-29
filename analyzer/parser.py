import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
    r'(?P<level>ERROR|INFO|WARNING) '
    r'(?P<message>.+)'
)

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None

    return {
        "timestamp": datetime.strptime(match.group("timestamp"), "%Y-%m-%d %H:%M:%S"),
        "level": match.group("level"),
        "message": match.group("message")
    }
