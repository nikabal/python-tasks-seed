"""
Sorting algorithms
"""


def builtin_sort(data):
    
    if isinstance(data, list):
        data.sort()
    else:  # assume it is counting container
        # TODO: скормить корректно, или оставить эту идею, и
        # сделать less & swap
        data._array.sort()


def bubble_sort(data):

    n = len(data)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break


def quick_sort(data, low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(data) - 1
    
    if low < high:
        pi = _partition(data, low, high)
        quick_sort(data, low, pi - 1)
        quick_sort(data, pi + 1, high)


def _partition(data, low, high):

    pivot = data[high]
    i = low - 1
    
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1