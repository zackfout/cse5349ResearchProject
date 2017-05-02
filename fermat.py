import random
import time
import numpy as np
import sieve

def fermat(n, k):
    for i in range(k):
        a = random.randrange(2, n)
        if pow(a, n-1, n) != 1:
            return False

    return True

def fermatBigO(limit, k):
    primes = sieve.sieveOfEratosthenes(limit)
    primes.pop(0)
    runningTime = list()

    for p in primes:
        start = time.time()
        fermat(p, k)
        end = time.time()
        runningTime.append((end - start))

    return {'n': primes, 't': runningTime}
