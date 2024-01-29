#!/usr/bin/python3
"""this is UTF-8 validator module"""


def validUTF8(data):
    """this function validates UTF-8 encoding"""
    for i in data:
        binary = bin(i)
        try:
            eval(binary).to_bytes(1, 'big').decode()
        except OverflowError:
            return False
    return True
