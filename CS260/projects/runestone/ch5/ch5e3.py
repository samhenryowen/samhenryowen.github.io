def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                newlist = []
                for _ in range(0,midpoint):
                    newlist.append(alist[_])
                return binarySearch(newlist, item)
            else:
                newlist = []
                for _ in range(midpoint+1, len(alist)):
                    newlist.append(alist[_])
                return binarySearch(newlist, item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
