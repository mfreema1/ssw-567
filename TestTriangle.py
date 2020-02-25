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
    """
    Verify that the Triangle class performs as expected.
    """

    def test_right_triangle_a(self):
        """
        Test ordering of a right triangle
        """
        self.assertEqual(classify_triangle(3, 4, 5),
                         ('Scalene', 'Right'),
                         '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """
        Test ordering of a right triangle with swapped ordering
        """
        self.assertEqual(classify_triangle(5, 3, 4),
                         ('Scalene', 'Right'),
                         '5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        """
        Test an equilateral triangle
        """
        self.assertEqual(classify_triangle(2, 2, 2),
                         ('Equilateral', 'Non-Right'),
                         '2,2,2 should be equilateral')

    def test_isosceles_triangles(self):
        """
        Test an isosceles triangle
        """
        self.assertEqual(classify_triangle(4, 5, 5),
                         ('Isosceles', 'Non-Right'),
                         '4, 5, 5 should be isosceles')

    def test_scalene_triangles(self):
        """
        Test a scalene triangle
        """
        self.assertEqual(classify_triangle(2, 3, 4),
                         ('Scalene', 'Non-Right'),
                         '2, 3, 4 should be isosceles')

    def test_not_a_triangle(self):
        """
        Test a triangle that is not possible to close
        """
        with self.assertRaises(ValueError, msg='1, 1, 100 is not a valid triangle'):
            classify_triangle(1, 1, 100)

    def test_negative_side_lengths(self):
        """
        Test a triangle with a negative side length
        """
        with self.assertRaises(ValueError, msg='-1, 1, 1 contains a negative side distance'):
            classify_triangle(-1, 1, 1)

    def test_wrong_argument_types(self):
        """
        Test a triangle with incorrect parameter type
        """
        with self.assertRaises(ValueError, msg='foo, bar, and baz are not integers'):
            classify_triangle('foo', 'bar', 'baz')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
