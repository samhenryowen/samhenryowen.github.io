from timeit import Timer

# Create dictionary of lower case chars with corresponding unicode values
# t1 times adding a single item to the dictionary
# t2 times getting a single value from the dictionary with key i

x = {}
for i in range(97,123):
    t1 = Timer("x.update({i: chr(i)})", "from __main__ import x,i")
    t2 = Timer("x.get(i)", "from __main__ import x,i")
    xt = t1.timeit(number=1)
    yt = t2.timeit(number=1)
    print("Key:", i ,"Value:", x[i], "  Set Timer:", "%f" %xt, "  Get Timer:", "%f" %yt)
