#!/usr/bin/python3
"""Log Parsing"""
import sys


def print_msg(status_codes, file_size):
    """print the message"""
    print('File size: {:d}'.format(file_size))
    for key, val in status_codes.items():
        if val != 0:
            print('{:s}: {:d}'.format(key, val))

file_size = 0
status_codes = {
    '200': 0, '301': 0,
    '400': 0, '401': 0,
    '403': 0, '404': 0,
    '405': 0, '500': 0
}
count = 0
for line in sys.stdin:
    try:
        try:
            raw = line.split()
            file_size += int(raw[-1])
            status_codes[str(raw[-2])] += 1
            count += 1
            if count / 10 == 1:
                count = 0
                print_msg(status_codes, file_size)
                file_size = 0
                status_codes = {
                '200': 0, '301': 0,
                '400': 0, '401': 0,
                '403': 0, '404': 0,
                '405': 0, '500': 0
                }
        except BaseException:
            pass
    except KeyboardInterrupt:
        print_msg(status_codes, file_size)
