# Fraction Class
class Fraction:
    
    # Constructor
    # Sets the numerator equal to top, denominator equal to bottom
    def __init__(self, top, bottom):
        
        # check if top and bottom are both of type int
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise "Numerator and denominator must be of type int"
        
        # check for negative denominator then reassign negative value appropriately
        if top < 0 and bottom < 0:
            top = abs(top)
            bottom = abs(bottom)
        elif bottom < 0:
            top = -top
            bottom = abs(bottom)
            
        common = self.gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common
    
    # String method
    # Overrides the str method to properly print the fraction
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    # repr method
    def __repr__(self):
        return "num=" + str(self.num) + " den=" + str(self.den)
    
    # Greatest common denominator method
    def gcd(self,m,n):
        while m%n != 0:
            oldm = m
            oldn = n
            
            m = oldn
            n = oldm%oldn
        return n
    
    
    '''Get Methods'''
    # Get numerator method
    def get_num(self): return self.num
    numerator = property(get_num)
    
    # Get denominator method
    def get_den(self): return self.den
    denominator = property(get_den)
    
    
    '''Arithmetic Methods'''
    # Add method
    def __add__(self, otherfraction):
        
        if not isinstance(otherfraction, Fraction):
            otherfraction = Fraction(otherfraction, 1)
            
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        
        return Fraction(newnum, newden)
    
    # Right hand add method
    def __radd__(self, otherfraction):
        
        if not isinstance(otherfraction, Fraction):
            otherfraction = Fraction(otherfraction, 1)
        
        return self.__add__(otherfraction)
    
    # iadd
    def __iadd__(self, otherfraction):
        if not isinstance(otherfraction, Fraction):
            otherfraction = Fraction(otherfraction, 1)
        
        return self.__add__(otherfraction)  
    
    # Subtract method
    def __sub__(self, otherfraction):
        
        if not isinstance(otherfraction, Fraction):
            otherfraction = Fraction(otherfraction, 1)
            
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        
        return Fraction(newnum, newden)
    
    # Multiplication method
    def __mul__(self, otherfraction):
        
        if not isinstance(otherfraction, Fraction):
            otherfraction = Fraction(otherfraction, 1)
            
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        
        return Fraction(newnum, newden)
    
    # Division method
    def __truediv__(self, otherfraction):
        
        if not isinstance(otherfraction, Fraction):
            otherfraction = Fraction(otherfraction, 1)
            
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        
        return Fraction(newnum, newden)
    
    
    '''Relational Operator Methods'''
    # Equal method
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        
        return firstnum == secondnum
    
    # Not equal method
    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        
        return firstnum != secondnum
    
    # Less than method
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum < secondnum
    
    # Less than or equal method
    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum <= secondnum
    
    # Greater than method
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        
        return firstnum > secondnum
    
    # Greater or equal to method
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        
        return firstnum >= secondnum

    
    
f1 = Fraction(1,5)
f2 = Fraction(3,4)


print(repr(f1))
