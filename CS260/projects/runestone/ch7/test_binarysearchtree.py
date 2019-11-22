import unittest
import binarysearchtree as bst

mytree = bst.BinarySearchTree()
mytree[2] = "red"
mytree[6] = "black"
mytree[4] = "purple"
mytree[1] = "blue"
mytree[5] = "orange"
mytree[3] = "pink"
mytree[3] = "silver"
mytree[3] = "brown"

class Test_binarysearchtree(unittest.TestCase):
    def test_inOrder(self):
        test_list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(mytree.inOrder(), test_list)

    def test_root(self):
        self.assertEqual(mytree.root.key, 2)

    def test_size(self):
        self.assertEqual(len(mytree), 6)

    def test_override_key_value(self):
        self.assertEqual(mytree[3], "brown")

if __name__ == '__main__':
    unittest.main()