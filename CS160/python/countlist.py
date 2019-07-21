list = []

def countto():
    z = 0
    x = int(input("Count to? "))
    
    if x == 0:
        print("Enter a number greater than 0")
        countto()
        
    else:
        for i in range(x):
            z = z + 1
            list.append(z)
        print(list)
        list.clear()
        countto()

countto()