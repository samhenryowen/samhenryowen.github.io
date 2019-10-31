import unittest
import fraction


class TestFraction(unittest.TestCase):
    f1 = fraction.Fraction(1,1)
    f2 = fraction.Fraction(1,2)
    f3 = fraction.Fraction(1,3)
    f4 = fraction.Fraction(1,4)
    
    def test_add(self):
        result = self.f1 + self.f2
        self.assertEqual(result, fraction.Fraction(3,2))
        self.assertEqual((self.f4 + self.f4), self.f2)
        
    def test_radd(self):
        self.assertEqual((self.f4 + self.f4), self.f2)
        self.assertEqual((1 + self.f1), (self.f1 * 2))
        
    def test_sub(self):
        result = self.f1 - self.f2
        self.assertEqual(result, self.f2)
        self.assertEqual(self.f4, (self.f2 - self.f4))
        
    def test_mul(self):
        self.assertEqual((self.f1 * self.f2), self.f2)
        self.assertEqual((self.f2 * self.f2), self.f4)
        
    def test_div(self):
        self.assertEqual((self.f2 / self.f2), self.f1)
        self.assertEqual((self.f4 / self.f2), self.f2)
        
    def test_ne(self):
        self.assertNotEqual(self.f1, self.f2)
        self.assertNotEqual(self.f2, self.f3)
        
    def test_lt(self):
        self.assertTrue(self.f2 < self.f1)
        self.assertTrue(self.f3 < self.f2)
        
    def test_gt(self):
        self.assertTrue(self.f3 > self.f4)
        self.assertTrue(self.f2 > self.f3)
        
    def test_ge(self):
        self.assertTrue(self.f1 >= (self.f2 + self.f2))
        self.assertTrue(self.f2 >= (self.f4 + self.f4))
        

if __name__ == '__main__':
    unittest.main()