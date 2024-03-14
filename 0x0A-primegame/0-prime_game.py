#!/usr/bin/python3
""" The module for Prime Game """


def isWinner(x, nums):
    """
       The Function
    """
    if x < 1 or not nums:
        return None

    x_maria, x_ben = 0, 0

    n = max(nums)
    primes = [True for _ in range(1, n + 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        x_ben += primes_count % 2 == 0
        x_maria += primes_count % 2 == 1
    if x_maria == x_ben:
        return None
    return 'Maria' if x_maria > x_ben else 'Ben'
