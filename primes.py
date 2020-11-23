from math import sqrt


def sieve_of_eratosthenes(n):
    '''given an integer n, returns an array of all prime numbers below n.
    This uses the ancient Greek method Sieve of Eratonsthenes.'''

    primes = list(range(n + 1))
    # primes[:2] = [False, False]

    primes[0] = primes[1] = False
    for multiple in range(2, int(sqrt(n)) + 1):
        if primes[multiple]:
            for num in range(2*multiple, n+1, multiple):
                primes[num] = False
    return tuple(prime for prime in primes if prime is not False)


def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        for div in range(3, int(n**0.5) + 1, 2):
            if n % div == 0:
                return False
    return True


if __name__ == '__main__':
    from time import time

    n = 10000000
    print(f'Testing timing of methods for calculating primes below {n}.')
    print()

    start = time()
    billion_primes = sieve_of_eratosthenes(n)
    duration = time() - start

    print(f'Sieve of Eratosthenes: {duration}')
