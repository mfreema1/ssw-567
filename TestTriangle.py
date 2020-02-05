# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3, 4, 5), ('Scalene', 'Right'), '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5, 3, 4), ('Scalene', 'Right'), '5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(2, 2, 2), ('Equilateral', 'Non-Right'), '2,2,2 should be equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classify_triangle(4, 5, 5), ('Isosceles', 'Non-Right'), '4, 5, 5 should be isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classify_triangle(2, 3, 4), ('Scalene', 'Non-Right'), '2, 3, 4 should be isosceles')

    def testNotATriangle(self):
        with self.assertRaises(ValueError, msg='1, 1, 100 is not a valid triangle'):
            classify_triangle(1,1, 100)

    def testNegativeSideLengths(self):
        with self.assertRaises(ValueError, msg='-1, 1, 1 contains a negative side distance'):
            classify_triangle(-1, 1, 1)

    def testWrongArgumentTypes(self):
        with self.assertRaises(ValueError, msg='foo, bar, and baz are not integers'):
            classify_triangle('foo', 'bar', 'baz')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
