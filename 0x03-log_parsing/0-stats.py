#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
including total file size and counts of HTTP status codes.
"""
import sys
import signal


def process_line(line, total_size, status_counts):
    """
    Process a single log line to extract metrics.
    :param line: A single log entry line.
    :param total_size: Current total file size.
    :param status_counts: Dictionary holding counts of status codes.
    :return: Updated total_size and status_counts.
    """
    parts = line.split()
    if len(parts) < 9:
        return total_size, status_counts

    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
    except ValueError:
        return total_size, status_counts

    if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1
    total_size += file_size
    return total_size, status_counts


def print_statistics(total_size, status_counts):
    """
    Print the accumulated statistics.
    :param total_size: Current total file size.
    :param status_counts: Dictionary holding counts of status codes.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def main():
    """
    Main function to read stdin and compute metrics.
    """
    total_size = 0
    status_counts = {}
    line_count = 0

    def handle_interrupt(signal, frame):
        """
        Handle keyboard interrupt signal to print
        statistics before exiting.
        """
        print_statistics(total_size, status_counts)
        sys.exit(0)
    signal.signal(signal.SIGINT, handle_interrupt)
    for line in sys.stdin:
        total_size, status_counts = process_line(
                                            line,
                                            total_size,
                                            status_counts
                                            )
        line_count += 1
        if line_count % 10 == 0:
            print_statistics(total_size, status_counts)
    if line_count % 10 != 0:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
