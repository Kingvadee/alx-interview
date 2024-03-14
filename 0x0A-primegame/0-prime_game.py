#!/usr/bin/python3

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n+1) if primes[i]]

def isWinner(x, nums):
    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        maria_turn = True
        while primes:
            if maria_turn:
                pick = primes.pop(0)
                for i in range(pick, n+1, pick):
                    if i in primes:
                        primes.remove(i)
                maria_turn = False
            else:
                pick = primes.pop(0)
                for i in range(pick, n+1, pick):
                    if i in primes:
                        primes.remove(i)
                maria_turn = True
        if maria_turn:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1
    
    max_wins = max(wins.values())
    if list(wins.values()).count(max_wins) == 1:
        return max(wins, key=wins.get)
    else:
        return None

# Test the function
print("Winner: {}".format(isWinner(3, [4, 5, 1])))

