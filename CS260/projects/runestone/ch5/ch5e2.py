import timeit
from random import randint

def binarySearch_it(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

def binarySearch_re(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch_re(alist[:midpoint], item)
            else:
                return binarySearch_re(alist[midpoint + 1:], item)

def it_time():
    it_setup = '''
from __main__ import binarySearch_it, testlist
from random import randint'''

    it_code = '''
binarySearch_it(testlist, randint(0,999))
'''

    times = timeit.repeat(setup=it_setup,
                          stmt=it_code,
                          repeat=10,
                          number=10000)
    print('Iterative binary search time: {}'.format(min(times)))


def re_time():
    re_setup = '''
from __main__ import binarySearch_re, testlist
from random import randint'''

    re_code = '''
binarySearch_re(testlist, randint(0,999))
'''

    times = timeit.repeat(setup=re_setup,
                          stmt=re_code,
                          repeat=10,
                          number=10000)
    print('Recursive binary search time: {}'.format(min(times)))


testlist = [randint(0,999) for _ in range(100)]

it_time()
re_time()