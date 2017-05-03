import time
import random
import numpy as np
import sieve

def solovayStrassen(n, k):
	if n == 2:
		return True
	if not n & 1:
		return False

	def legendre(a, p):
		if p < 2:
			raise ValueError('p must not be < 2')
		if (a == 0) or (a == 1):
			return a
		if a % 2 == 0:
			r = legendre(a / 2, p)
			if p * p - 1 & 8 != 0:
				r *= -1
		else:
			r = legendre(p % a, a)
			if (a - 1) * (p - 1) & 4 != 0:
				r *= -1
		return r

	for i in np.arange(k):
		a = random.randrange(2, n - 1)
		x = legendre(a, n)
		y = pow(a, (n - 1) / 2, n)
		if (x == 0) or (y != x % n):
			return False

	return True

def soloveyStrassenBigO(limit, k):
    primes = sieve.sieveOfEratosthenes(limit)
    primes.pop(0)
    primes.pop(0)
    runningTime = list()

    for p in primes:
        start = time.time()
        solovayStrassen(p, k)
        end = time.time()
        runningTime.append((end - start))

    return {'n': primes, 't': runningTime}
