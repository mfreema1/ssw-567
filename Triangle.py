"""
A collection of functions to help with classifying triangles
"""

from collections import Counter

def is_right_triangle(first, second, third):
    """
    Determine if a set of sides constitutes a right triangle
    """
    sorted_squares = list(map(lambda num: pow(num, 2), sorted([first, second, third])))
    return sum(sorted_squares[:2]) == sorted_squares[2]

def is_possible_triangle(first, second, third):
    """
    Determine if a set of sides could constitute a triangle
    """
    sorted_sides = sorted([first, second, third])
    return sum(sorted_sides[:2]) > sorted_sides[2]

def num_distinct(nums):
    """
    Determine the number of distinct elements in a list
    """
    counter = Counter()
    for num in nums:
        counter[num] += 1
    return len(counter.keys())

def classify_triangle(first, second, third):
    """
    Main method of module.  Export information about a set of sides
    """
    if not(isinstance(first, int) and isinstance(second, int) and isinstance(third, int)):
        raise ValueError("Arguments must be integers")

    if not(first > 0 and second > 0 and third > 0):
        raise ValueError("Side lengths cannot be negative")

    if not is_possible_triangle(first, second, third):
        raise ValueError("Not a triangle")

    types = {
        1: 'Equilateral',
        2: 'Isosceles',
        3: 'Scalene'
    }

    is_right = is_right_triangle(first, second, third)
    distinct_sides = num_distinct([first, second, third])

    right_string = 'Right' if is_right else 'Non-Right'

    return (types[distinct_sides], right_string)
