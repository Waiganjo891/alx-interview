#!/usr/bin/python3
"""
Log parser that reads from stdin line by line and computes metrics.
The script expects lines in the following format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
After every 10 lines and/or a keyboard interruption (CTRL + C), it prints:
- Total file size: sum of all file sizes
- Number of lines by status code, sorted in ascending order
"""
import sys
import signal


total_file_size = 0
status_codes_count = {
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


def print_stats():
    """
    Prints the statistics: total file size and counts for each status code.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))


def signal_handler(sig, frame):
    """Handles the keyboard interruption signal."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


for line in sys.stdin:
    line_count += 1
    parts = line.split()
    if len(parts) < 7:
        continue
    try:
        ip, _, _, date, request, status_code, file_size = parts[0],
        parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]
        status_code = int(status_code)
        file_size = int(file_size)
    except (ValueError, IndexError):
        continue
    total_file_size += file_size
    if status_code in status_codes_count:
        status_codes_count[status_code] += 1
    if line_count % 10 == 0:
        print_stats()
if line_count > 0:
    print_stats()
