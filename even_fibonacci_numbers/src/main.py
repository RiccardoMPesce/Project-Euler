import sys
import pytest

from fibonacci_calculator import fibonacci_calculator

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "TEST":
            pytest.main()
    
    fibonacci_sequence = fibonacci_calculator(4000000)
    print(sum([i for i in fibonacci_sequence if i % 2 == 0]))


if __name__ == "__main__":
    main()