from collections import Counter

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def is_right_triangle(a, b, c):
    sorted_squares = list(map(lambda num: pow(num, 2), sorted([a, b, c])))
    return sum(sorted_squares[:2]) == sorted_squares[2]

def is_possible_triangle(a, b, c):
    sorted_sides = sorted([a, b, c])
    return sum(sorted_sides[:2]) > sorted_sides[2]

def num_distinct(nums):
    counter = Counter()
    for num in nums:
        counter[num] += 1
    return len(counter.keys())

def classify_triangle(a, b, c):
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        raise ValueError("Arguments must be integers")

    if not(a > 0 and b > 0 and c > 0):
        raise ValueError("Side lengths cannot be negative")

    if not is_possible_triangle(a, b, c):
        raise ValueError("Not a triangle")

    types = {
        1: 'Equilateral',
        2: 'Isosceles',
        3: 'Scalene'
    }

    is_right = is_right_triangle(a, b, c)
    distinct_sides = num_distinct([a, b, c])

    right_string = 'Right' if is_right else 'Non-Right'

    return (types[distinct_sides], right_string)

    """
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
    """
