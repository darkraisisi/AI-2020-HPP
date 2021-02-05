import numpy as np
import time
import matplotlib.pyplot as plt

def bucketSort(lst:np.array):
    negLst = []
    posLst = []

    for num in lst:
        if num < 0:
            negLst.append(num*-1)
        else:
            posLst.append(num)
    
    del lst

    if len(negLst) > 0:
        negLst = distribution(negLst)
        negLst.reverse()
        negLst = [x*-1 for x in negLst]
    
    if len(posLst) > 0:
        posLst = distribution(posLst)

    return negLst + posLst


def distribution(lst):
    buckets = emptyBuckets()

    for i in range(1, len(str(max(lst))) + 1):
        for num in lst:

            digitLen = len(str(num))
            if i <= digitLen:
                rowPos = int(str(num)[-i])
                buckets[rowPos].append(num)
            else:
                buckets[0].append(num)

        lst = gathering(buckets)
        buckets = emptyBuckets()

    return lst


def gathering(lst):
    newList = []

    for subList in lst:
        newList = newList + subList
    return newList


def emptyBuckets():
    buckets = []

    for _ in range(0,10):
        buckets.append([])
    return buckets


def exerciseOne():
    lst = np.random.randint(999,size=40)
    ret = bucketSort(lst)
    print(ret)


def exerciseTwo():
    lengths = [10000, 20000, 30000, 100000, 200000, 300000]
    numberSizes = [999, 9999, 99999]

    times = []
    lists = []
    for i, size in enumerate(numberSizes, 0):
        times.append([])
        for n in lengths:
            lst = np.random.randint(-1000,size,size=n)

            startTime = time.time()
            sortedList = bucketSort(lst)
            timeDiff = time.time() - startTime
            print(f'Sorting N:{n} took {timeDiff}s')

            times[i].append(timeDiff)
            lists.append(sortedList)
    

    for i, _time in enumerate(times, 0):
        plt.plot(lengths,_time,'-o',label='0-'+str(numberSizes[i])+' random')

    return lists


def exerciseThree(lists):
    lengths = [10000, 20000, 30000, 100000, 200000, 300000]
    numberSizes = [999, 9999, 99999]

    times = []
    for i, size in enumerate(numberSizes, 0):
        times.append([])
        lists[i].reverse()
        for n in lengths:
            startTime = time.time()
            srt = bucketSort(np.asarray(lists[i]))
            timeDiff = time.time() - startTime
            print(f'Sorting N:{n} took {timeDiff}s')
            times[i].append(timeDiff)
    

    for i, _time in enumerate(times, 0):
        plt.plot(lengths,_time,'--o',label='0-'+str(numberSizes[i])+' reverse' )


lists = exerciseTwo()
exerciseThree(lists)

plt.xlabel('Array size')
plt.ylabel('Time in seconds')
plt.legend(title='Number sizes')
plt.show()