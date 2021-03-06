from random import shuffle
from matplotlib import pylab as plt
from datetime import datetime


def insertion(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while (i > -1) and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

def quick_sort(a):
    less = []
    equal = []
    greater = []
    if len(a) > 1:
        pivot = a[0]
        for x in a:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return a

def counting_sort(a):
    counts = [0 for i in range(max(a) + 1)]

    for el in a:
        counts[el] += 1

    for index in range(1, len(counts)):
        counts[index] = counts[index - 1] + counts[index]

    L = [0 for loop in range(len(a) + 1)]
    for el in a:
        index = counts[el] - 1
        L[index] = el
        counts[el] -= 1

    return L

def insertion_time(n):
    a = [i for i in range(n)]
    shuffle(a)
    start = datetime.now()
    insertion(a)
    return (datetime.now() - start).microseconds

def quick_sort_time(n):
    a = [i for i in range(n)]
    shuffle(a)
    start = datetime.now()
    quick_sort(a)
    return (datetime.now() - start).microseconds

def counting_sort_time(n):
    a = [i for i in range(n)]
    shuffle(a)
    start = datetime.now()
    counting_sort(a)
    return (datetime.now() - start).microseconds

plt.plot([10, 100, 1000, 10000], [insertion_time(10), insertion_time(100), insertion_time(1000), insertion_time(10000)])
plt.plot([10, 100, 1000, 10000], [quick_sort_time(10), quick_sort_time(100), quick_sort_time(1000), quick_sort_time(10000)])
plt.plot([10, 100, 1000, 10000], [counting_sort_time(10), counting_sort_time(100), counting_sort_time(1000), counting_sort_time(10000)])
plt.show()
