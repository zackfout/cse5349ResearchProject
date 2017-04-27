#!/usr/local/bin/python

import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import sieve
import trialDivision

def scaleNumber(unscaled, toMin, toMax, fromMin, fromMax):
    return (toMax - toMin) * (unscaled - fromMin) / (fromMax - fromMin) + toMin

def scaleList(l, toMin, toMax):
    return [scaleNumber(i, toMin, toMax, min(l), max(l)) for i in l]

def main():
    start = time.time()
    data = sieve.sieveBigO(100000)
    end = time.time()

    print 'sieveBigO Total Execution time: %s seconds' % (end - start)

    t = data['n'] * np.log(np.log(data['n']))
    t = scaleList(t, 0, 0.08)

    plt.figure(1)
    plt.plot(data['n'], t, label='t = n log log n')
    plt.plot(data['n'], data['t'], label='Sieve of Eratosthenes')
    plt.ylabel('Running Time (seconds)')
    plt.xlabel('Input Size (n)')
    plt.title('Time Complexity of the Sieve of Eratosthenes')
    plt.legend()
    plt.show()

    start = time.time()
    data = trialDivision.trialDivisionBigO(15)
    end = time.time()

    print 'Trial Division Total Execution time: %s seconds' % (end - start)

    t = np.exp(data['n'])
    t = scaleList(t, 0, 8)

    plt.figure(2)
    plt.plot(data['n'], t, label=r't = $e^n$')
    plt.plot(data['n'], data['t'], label='trial division')
    plt.ylabel('Running Time (seconds)')
    plt.xlabel('Input Size (n)')
    plt.title('Time Complexity of Trial Division')
    plt.xticks(np.arange(0, 16))
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
