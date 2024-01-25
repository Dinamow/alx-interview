#!/usr/bin/python3
"""Log Parsing"""
import sys


while True:
    file_size = 0
    status_codes = {
        '200': 0, '301': 0,
        '400': 0, '401': 0,
        '403': 0, '404': 0,
        '405': 0, '500': 0
    }
    for i in range(10):
        raw = sys.stdin.readline().split()
        file_size += int(raw[-1])
        status_codes[str(raw[-2])] += 1
    print('File size: {:d}'.format(file_size))
    for i in status_codes.keys():
        if status_codes[i] != 0:
            print('{:s}: {:d}'.format(i, status_codes[i]))
