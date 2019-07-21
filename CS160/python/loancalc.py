pv = float(input("How much is the loan for? "))
r = float(input("What is the rate per period? "))
n = int(input("How many periods? "))

p = ((r*pv)/(1-(1+r)**-1))

print("Your payment is", p)