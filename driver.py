#!/usr/local/bin/python

import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import wilson
import sieve
import trialDivision
import fermat
import millerRabinTest

def scaleNumber(unscaled, toMin, toMax, fromMin, fromMax):
    return (toMax - toMin) * (unscaled - fromMin) / (fromMax - fromMin) + toMin

def scaleList(l, toMin, toMax):
    return [scaleNumber(i, toMin, toMax, min(l), max(l)) for i in l]

def main():
    # start = time.time()
    # data = sieve.sieveBigO(100000)
    # end = time.time()
    #
    # print 'sieveBigO Total Execution time: %s seconds' % (end - start)
    #
    # t = data['n'] * np.log(np.log(data['n']))
    # t = scaleList(t, 0, 0.08)
    #
    # plt.figure(1)
    # plt.plot(data['n'], t, color='C0', label='t = n log log n')
    # plt.scatter(data['n'], data['t'], color='C1', label='Sieve of Eratosthenes')
    # plt.ylabel('Running Time (seconds)')
    # plt.xlabel('Input Size (n)')
    # plt.title('Time Complexity of the Sieve of Eratosthenes')
    # plt.legend()
    # plt.show()

    # start = time.time()
    # data = trialDivision.trialDivisionBigO(15)
    # end = time.time()
    #
    # print 'trialDivisionBigO Total Execution time: %s seconds' % (end - start)
    #
    # t = np.exp(data['n'])
    # t = scaleList(t, 0, 8)
    #
    # plt.figure(2)
    # plt.plot(data['n'], t, label=r't = $e^n$')
    # plt.plot(data['n'], data['t'], label='trial division')
    # plt.ylabel('Running Time (seconds)')
    # plt.xlabel('Input Size (n)')
    # plt.title('Time Complexity of Trial Division')
    # plt.xticks(np.arange(0, 16))
    # plt.legend()
    # plt.show()

    # start = time.time()
    # data = fermat.fermatBigO(200000, 100)
    # end = time.time()
    #
    # print 'fermatBigO Total Execution time: %s seconds' % (end - start)
    #
    # t = 100 * np.log(data['n']) * np.log(data['n']) * np.log(data['n'])
    # t  = scaleList(t, 0.00012, 0.00022)
    #
    # plt.figure(3)
    # plt.plot(data['n'], t, color='C0', label=r't = $log^3(n)$')
    # plt.scatter(data['n'], data['t'], color='C1', label='fermat test')
    # plt.ylabel('Running Time For 100 Tests (seconds)')
    # plt.xlabel('Input Size (n)')
    # plt.title('Time Complexity of Fermat\'s Test')
    # plt.legend()
    # plt.ylim([0, 0.0003])
    # plt.show()

    # start = time.time()
    # data = millerRabinTest.millerRabinBigO(10000, 100)
    # end = time.time()
    #
    # print 'millerRabinBigO Total Execution time: %s seconds' % (end - start)
    #
    # plt.figure(4)
    # plt.scatter(data['n'], data['t'], color='C1', label='miller-rabin test')
    # plt.ylabel('Running Time For 100 Tests (seconds)')
    # plt.xlabel('Input Size (n)')
    # plt.title('Time Complexity of Miller-Rabin Test')
    # plt.legend()
    # plt.show()

if __name__ == '__main__':
    main()
