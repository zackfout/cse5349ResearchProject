import time
import numpy as np

def wilson(n):
    factorial = 1
    for i in np.arange(1, n):
        factorial = (factorial * i) % n
    return (factorial == n-1)

def wilsonBigO(limit):
    inputSize = np.arange(1, limit, 1)
    runningTime = list()

    start = time.time()
    for i in inputSize:
        wilson(i)
        end = time.time()
        runningTime.append((end - start))

    return {'n': inputSize, 't': runningTime}
