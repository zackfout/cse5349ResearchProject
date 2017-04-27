import numpy as np
import time

def sieveOfEratosthenes(n):
    limit = n + 1
    composites = set()
    primes = list()

    for i in range(2, limit):
        if i in composites:
            continue

        for j in range(i * i, limit, i):
            composites.add(j)

        primes.append(i)

    return primes

def sieveBigO(limit):
    inputSize = np.arange(10, limit, 100)
    runningTime = list()

    for i in inputSize:
        start = time.time()
        sieveOfEratosthenes(i)
        end = time.time()
        runningTime.append((end - start))

    return {'n': inputSize, 't': runningTime}
