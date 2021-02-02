def quickSort(lst) -> list:
    if len(lst) <= 1:
        if len(lst) == 0:
            return []
        return lst

    low, high, pivot = partition(lst)
    return quickSort(low) + [pivot] + quickSort(high)


def partition(lst):
    low = []
    high = []
    for num in lst[1:]:
        if num <= lst[0]:
            low.append(num)
        else:
            high.append(num)

    return low, high, lst[0]

ret = quickSort([3,7,1,8,3,5,34,23,87,23,67,54,12])
print(ret)

"""
Big O from analysis:
n*log(n), for each step half?
"""