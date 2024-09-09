def subtract(a, b):
    return a - b

import unittest

class TestMathFunctions(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 5), 5)
        
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-10, -5), -5)
        
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(-5, 3), -8)
        
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)

if __name__ == '__main__':
    unittest.main()

