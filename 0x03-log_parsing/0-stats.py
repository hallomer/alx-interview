#!/usr/bin/python3
"""Log parsing."""
import sys
import signal
import re

# Initialize metrics
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

# Regex to match the log format
log_regex = re.compile(
    r'^\d+\.\d+\.\d+\.\d+ - \[.*?\] "GET /projects/260 HTTP/1.1" '
    r'(\d{3}) (\d+)$'
)


def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles the keyboard interrupt signal to print statistics."""
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_regex.match(line.strip())
        if match:
            status_code, file_size_str = match.groups()
            file_size = int(file_size_str)
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
except Exception:
    pass
finally:
    print_stats()
