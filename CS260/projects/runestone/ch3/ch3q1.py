from timeit import Timer

# t1 times the use of index operator on x for each element in the list
# prints the index and the time to perform the operation a single time

for i in range(100):
    t1 = Timer("x[i]", "from __main__ import x,i")
    x = list(range(100))
    xt = t1.timeit(number=1)
    print(x[i], "%f" % xt)
