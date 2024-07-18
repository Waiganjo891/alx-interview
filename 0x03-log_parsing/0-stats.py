#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics:
- Total file size
- Count of status codes
(200, 301, 400, 401, 403, 404, 405, 500)
"""

import sys
import signal


total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_statistics():
    """
    Prints the accumulated statistics
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """
    Handles keyboard interruption signal to print statistics
    """
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 7:
            continue
        ip_address,
        _,
        date,
        request,
        _,
        status_code_str,
        file_size_str = parts
        try:
            status_code = int(status_code_str)
            file_size = int(file_size_str)
        except ValueError:
            continue
        if status_code in status_code_counts:
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
