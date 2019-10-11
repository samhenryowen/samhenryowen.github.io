import random

class Sorter:
    
    def __init__(self):
        self.numlist = [random.randint(0,1000) for _ in range(100)]
    
    # find minimum number O(n)
    def sort1(self):
        min_num = None
        for _ in self.numlist:
            if min_num == None:
                min_num = _
                
            if _ < min_num:
                min_num = _
                
        return min_num
    
    # find minimum number O(n^2)
    def sort2(self):
        min_num = None
        
        for a in self.numlist:
            if min_num == None:
                min_num = a
            
            for b in self.numlist:  
                if b < min_num:
                    min_num = b
                    
        return min_num
                
            

class Main:
    test = Sorter()
    print(test.sort1())
    print(test.sort2())
