#!/usr/bin/python3
"""this is UTF-8 validator module"""


def validUTF8(data):
    """this function validates UTF-8 encoding"""
    for i in data:
        if i > 255:
            return False
    return True
