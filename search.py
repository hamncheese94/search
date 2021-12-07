'''
Author: Chris Alexander
Date: 9/24/21
Purpose: This program benchmarks performance of linear, jump, and binary searches
of data elements.
'''
from decimal import Decimal
from time import perf_counter
import random
from math import sqrt
from math import floor
from math import log10

def jump_search(data, target): 
    count = sqrt(len(data))
    prev = 0
    while data[int(min(count, len(data))-1)] < target:
        prev = count
        count += sqrt(len(data))
        if prev >= len(data):
            return False
    while data[int(prev)] < target:
        prev += 1
        if prev == min(count, len(data)):
            return False
    if data[int(prev)] == target:
        return True
    return False

def linear_search(data,target):
    '''linear search function'''
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

def binary_search(data, target):
    first = 0
    last = len(data) - 1
    middle = 0
    while first <= last:
        middle = (last + first) // 2
        if data[middle] < target:
            first = middle + 1
        elif data[middle] > target:
            last = middle - 1
        else:
            return True
    return False

#time and round functions
def linear_report(data, target):
    '''linear search report'''
    start = perf_counter()
    linear_search(data, target)
    stop = perf_counter()
    num = Decimal(stop - start)
    sigfigs = 2
    round_num =  round(num, sigfigs - int(floor(log10(abs(num)))) - 1)
    print("time to element [" + str(target) + "]: " + str(round_num) + "s")

def jump_report(data, target):
    '''jump search report'''
    start = perf_counter()
    jump_search(data, target)
    stop = perf_counter()
    num = Decimal(stop - start)
    sigfigs = 2
    round_num =  round(num, sigfigs - int(floor(log10(abs(num)))) - 1)
    print("time to element [" + str(target) + "]: " + str(round_num) + "s")

def binary_report(data, target):
    #binary search report
    start = perf_counter()
    binary_search(data, target)
    stop = perf_counter()
    num = Decimal(stop - start)
    sigfigs = 2
    round_num =  round(num, sigfigs - int(floor(log10(abs(num)))) - 1)
    print("time to element [" + str(target) + "]: " + str(round_num) + "s")

def main():
    random.seed(207) #input
    data = random.sample(range(5_000_000),k=5_000_000)
    data.sort()
    target1 = len(data) - len(data)#first
    target2 = len(data) // 2#middle
    target3 = len(data)#last
    target4 = target1 - 1#missing

    print("--------------------------------------------")
    print("linear search benchmark(" + str(len(data)) + " elements):")
    print("--------------------------------------------")
    linear_report(data, target1)
    linear_report(data, target2)
    linear_report(data, target3)
    linear_report(data, target4)

    print("--------------------------------------------")
    print("jump search benchmark(" + str(len(data)) + " elements):")
    print("--------------------------------------------")
    jump_report(data, target1)
    jump_report(data, target2)
    jump_report(data, target3)
    jump_report(data, target4)

    print("--------------------------------------------")
    print("binary search benchmark(" + str(len(data)) + " elements):")
    print("--------------------------------------------")
    binary_report(data, target1)
    binary_report(data, target2)
    binary_report(data, target3)
    binary_report(data, target4)

if __name__ == "__main__":
    main()
    