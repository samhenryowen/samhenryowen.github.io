height = int(input('Enter height of tree: '))

row = 0

while row < height:  

    count = 0
    while count < row+1:
        print(end='*')
        count += 1
           
    print()
    row += 1

while height > 0:
    
    count = 1
    while count < height:
        print(end='*')
        count += 1
    
    print()
    height -= 1