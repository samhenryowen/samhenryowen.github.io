sumf = float()
f = 1
i = 0
while f > 0:
    f = float(input("Enter a float value: "))
    if f > 0:
        i = i+1
        if i == 1:
            minimum = f
            maximum = f
        if f > maximum:
            maximum = f
        if f < minimum:
            minimum = f
        sumf = sumf+f
        average = sumf/i
    
print('max',maximum,'\nmin',minimum,'\nsum',sumf,'\naverage',average)
