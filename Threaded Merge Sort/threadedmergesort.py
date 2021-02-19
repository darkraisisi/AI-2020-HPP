from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt
import time
import math
import random

def mergeSort(x:list):
    if len(x) > 1:
        mid = len(x)//2

        L = x[:mid]
        R = x[mid:]

        L = mergeSort(L)
        R = mergeSort(R)
        x = merge(L,R)
        return x
    else:
        return x


def merge(L:list, R:list):
    i = j = 0
    x = []

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            x.append(L[i]) 
            i += 1
        else:
            x.append(R[j])
            j += 1

    while i < len(L):
        x.append(L[i])
        i += 1

    while j < len(R):
        x.append(R[j])
        j += 1
    return x


def splitList(lst:list,n:int):
    # n chunks
    n = math.ceil(len(lst) / n)
    ret = []
    for i in range(0, len(lst),n):
        ret.append(lst[i:i+n])
    return ret


def test(nWorkers:int,length:int):
    randomList = [random.randint(0,9999) for _ in range(0,length)]
    splt = splitList(randomList, nWorkers)

    with ThreadPoolExecutor(max_workers=nWorkers) as executor:
        results = executor.map(mergeSort, splt)

    results = list(results)

    while len(results) > 1:
        res = []
        for i in range(0,len(results)-1,2):
            res.append(merge(results[i],results[i+1]))

        results = res
    # print(results[0])


if __name__ == '__main__':
    results = []
    lengths = [1000, 10000, 100000]
    for i, length in enumerate(lengths,0):
        results.append([])
        for j in range(1,6):
            nWorkers = 2 ** j
            startTime = time.time()
            test(nWorkers, length)
            results[i].append(time.time() - startTime)
    
    time = [ 2 ** i for i in range(1,6)]
    for i, length in enumerate(lengths,0):
        plt.plot(time, results[i], '-o', label=str(length))
    
    plt.legend()
    plt.show()