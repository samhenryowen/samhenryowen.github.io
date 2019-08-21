sumf = float()
for i in range(20):
    f = float(input("Enter a float value: "))
    if i == 0:
        minimum = f
        maximum = f
    if f > maximum:
        maximum = f
    if f < minimum:
        minimum = f
    sumf = sumf+f
    average = sumf/(i+1)
    
print('max',maximum,'\nmin',minimum,'\nsum',sumf,'\naverage',average)