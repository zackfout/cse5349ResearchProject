import numpy as np
import time
import sieve

def trialDivision(n):
    if n < 2:
        return list()

    factors = list()

    for p in sieve.sieveOfEratosthenes(int(n ** 0.5)):
        if p * p > n: break
        while n % p == 0:
            factors.append(p)
            n //= p

    if n > 1:
        factors.append(n)

    if len(factors) == 1:
        return True
    else:
        return False

def trialDivisionBigO(limit):
    inputSize = np.arange(0, limit, 1)
    runningTime = list()

    for i in inputSize:
        start = time.time()
        trialDivision(10**i)
        end = time.time()
        runningTime.append((end - start))

    return {'n': inputSize, 't': runningTime}
