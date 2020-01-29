from hw01 import classify_triangle

def test_equilateral():
    assert classify_triangle(1, 1, 1) == ('equilateral', False)

def test_isosceles():
    assert classify_triangle(1, 2, 1) == ('isosceles', False)

def test_scalene():
    assert classify_triangle(1, 2, 3) == ('scalene', False)

def test_right():
    assert classify_triangle(3, 4, 5) == ('scalene', True)

def test_not_right():
    assert classify_triangle(1, 1, 1) == ('equilateral', False)