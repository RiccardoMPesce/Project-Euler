from src.fibonacci_calculator import fibonacci_calculator

def test_fibonacci_pe():
    assert fibonacci_calculator(10) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]