def isRoundWinner(n):
    '''find round winner'''
    # Generate a list of consecutive integers starting from 1 up to n
    numbers = [i for i in range(1, n + 1)]
    # Prime numbers available to choose
    primes = sieve_of_eratosthenes(n)
    # Initialize the turn counter
    turn = 0
    # While there are prime numbers available to choose
    while primes:
        # Determine the current player
        current_player = turn % 2
        # Select the largest prime number available
        selected_prime = max(primes)
        # Remove the selected prime number and its multiples from the list
        for i in range(selected_prime, n + 1, selected_prime):
            if i in numbers:
                numbers.remove(i)
        # If the current player cannot make a move, return the other player as the winner
        if not any(i % p == 0 for p in primes for i in numbers):
            return 'Ben' if current_player == 0 else 'Maria'
        # Remove the selected prime number from the available primes
        primes.remove(selected_prime)
        # Increment the turn counter
        turn += 1
    # If no prime numbers are available, the current player wins
    return 'Maria' if current_player == 0 else 'Ben'

def isWinner(x, nums):
    '''finds the winner'''
    # Initialize the winner counter
    winner_counter = {'Maria': 0, 'Ben': 0}
    # Iterate over each round
    for n in nums:
        # Determine the winner of the round
        round_winner = isRoundWinner(n)
        # Update the winner counter
        winner_counter[round_winner] += 1
    # Determine the overall winner
    if winner_counter['Maria'] > winner_counter['Ben']:
        return 'Maria'
    elif winner_counter['Ben'] > winner_counter['Maria']:
        return 'Ben'
    else:
        return None

def sieve_of_eratosthenes(n):
    '''Sieve of Eratosthenes algorithm to find prime numbers up to n'''
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n + 1) if primes[i]]

