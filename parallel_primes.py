from multiprocessing import Pool
from pickle import dump
from math import sqrt
from time import time


n = 1000000000  # 1B
n = 10000000  # 10M

sieve = [True] * (n+1)
sieve[0] = sieve[1] = False


def falsify_multiples(multiple):
    if sieve[n] is False:
        return
    for num in range(2*multiple, n+1, multiple):
        sieve[num] = False


if __name__ == '__main__':
    start = time()

    with Pool(5) as p:
        p.map(falsify_multiples, range(2, int(sqrt(n)) + 1))
        # print(p.map(f, [1, 2, 3]))

    primes = tuple(i for i, prime in enumerate(sieve) if prime is not False)

    duration = time() - start

    print(f'Duration of multiprocessing method: {duration}')

    # text_file = open('primes_under_1B.txt', 'w+')
    # pkl_file = open('primes_under_1B.pkl', 'wb+')

    # dump(primes, pkl_file)

    # for p in primes:
    #     text_file.write(str(p) + '\n')
