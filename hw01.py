from collections import Counter
from math import pow

def is_right_triangle(a, b, c):
    sorted_squares = list(map(lambda num: pow(num, 2), sorted([a, b, c])))
    print(sorted_squares)
    return sum(sorted_squares[:2]) == sorted_squares[2]

def num_distinct(nums):
    counter = Counter()
    for num in nums:
        counter[num] += 1
    return len(counter.keys())

def classify_triangle(a, b, c):
    types = {
        1: 'equilateral',
        2: 'isosceles',
        3: 'scalene'
    }

    is_right = is_right_triangle(a, b, c)
    distinct_sides = num_distinct([a, b, c])
    return (types[distinct_sides], is_right)