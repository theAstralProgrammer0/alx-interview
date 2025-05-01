#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 1409029840
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 22273783945
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

