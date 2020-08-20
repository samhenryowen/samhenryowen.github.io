import math

def baseChange(decimal_value, base):
    result = decimal_value
    new_base_value = []
    ansbin = []
    
    while result != 0:
        ansbin.extend(math.modf(result / base))
        
        result = ansbin.pop()
        new_base_value.append(str((int(round(ansbin.pop() * base)))))
        
    new_base_value.reverse()    
    return int(''.join(new_base_value))

print(baseChange(100, 2))