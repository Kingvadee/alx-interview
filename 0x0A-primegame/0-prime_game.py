def isRoundWinner(n):
    '''find round winner'''
    list = [i for i in range(1, n + 1)]
    prime = -1
    for idx, num in enumerate(list):
        # if already picked prime num then
        # find if num is multipl of the prime num
        if prime != -1:
            if num % prime == 0:
                list[idx] = -1
        # else check is num is prime then pick it
        else:
            if isPrime(num):
                prime = num
                list[idx] = -1
    # if failed to pick then current player lost
    if prime == -1:
        return 'Ben'
    else:
        return 'Maria'

def isWinner(x, nums):
    '''finds the winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i])
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isPrime(n):
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Not prime if divisible by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return False
        return True

