import time
import random
import numpy as np
import sieve

def millerRabin(n, k):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False

    s = 0
    d = n-1
    while d % 2 == 0:
        s += 1
        d //= 2

    for i in range(k):
        a = random.randrange(2, n-1)
        x = (a**d) % n
        if x == 1: continue
        for j in range(s):
            if x == n-1: break
            x = (x * x) % n
        else:
          return False

    return True

def millerRabinBigO(limit, k):
    primes = sieve.sieveOfEratosthenes(limit)
    runningTime = list()

    for p in primes:
        start = time.time()
        millerRabin(p, k)
        end = time.time()
        runningTime.append((end - start))

    return {'n': primes, 't': runningTime}
