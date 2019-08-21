dupe = False

n1 = int(input("enter number: "))
n2 = int(input("enter number: "))
if n1 == n2:
    dupe = True
n3 = int(input("enter number: "))
if n3 == n1 or n3 == n2:
    dupe = True
n4 = int(input("enter number: "))
if n4 == n3 or n4 == n2 or n4 == n1:
    dupe = True
n5 = int(input("enter number: "))
if n5 == n4 or n5 == n3 or n5 == n2 or n5 == n1:
    dupe = True
    
if dupe == True:
    print("duplicate numbers found")
else:
    print("no duplicate numbers found")

