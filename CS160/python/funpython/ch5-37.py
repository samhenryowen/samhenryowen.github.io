height = int(input('Enter height of tree: '))

row = 0

while row < height:
    
    count = 0
    while count < height - row-1:
        print(end=' ')
        count += 1

    count = 0
    while count < row+1:
        print(end='*')
        count += 1
           
    print()
    row += 1

row = 0

while row < height:
    
    
    count = 0
    while count < row+1:
       print(end=' ')
       count += 1
   
   
    count = 0
    while count < height - row -1:
        print(end='*')
        count += 1
    
    print()
    row += 1