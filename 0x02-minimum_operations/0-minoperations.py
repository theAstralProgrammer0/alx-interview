#!/usr/bin/python3
"""This module finds the minimum number of operations of performing a task
"""


def isPrime(n):
    """This function finds the prime value of a number.

        Args:
            n => number
        Return:
            Bool
    """
    for num in range(2, n):
        if n % num == 0:
            return False
    return True


def primeFactors(n):
    """This function finds the prime factors of a number

        Args:
            n => number
        Return:
            factors => List of Prime Factors (Integers)
    """
    # Initialization
    factors = []

    # Iteration
    while n != 1:
        for num in range(2, n + 1):
            if n % num == 0 and isPrime(num):
                factors.append(num)
                n //= num
                break
    return factors


def minOperations(n):
    """This function finds the minimum number of operations

        Args:
            n => task magnitude
        Return:
            Integer => Sum of Prime Factors
    """
    return sum(primeFactors(n))
