#!/usr/bin/python3

"""Prime Game Interview Question."""


def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to n using the Sieve
    of Eratosthenes.
    """
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[0], prime[1] = False, False
    return prime


def count_primes_up_to(prime):
    """Count the number of primes up to each index."""
    count = 0
    prime_count = [0] * len(prime)
    for i in range(len(prime)):
        if prime[i]:
            count += 1
        prime_count[i] = count
    return prime_count


def isWinner(x, nums):
    """Determine who the winner of the game is."""
    if x == 0 or x == 1:
        return None

    n = max(nums)
    prime = sieve_of_eratosthenes(n)
    prime_count = count_primes_up_to(prime)

    player1 = sum(prime_count[num] % 2 == 1 for num in nums)

    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
