import pytest
import sys
import pytest

from multiple_of_3_and_5 import multiple_of_3_and_5

def main():
    print(f"Calling {sys.argv[0]}")

    if len(sys.argv) > 1 and sys.argv[1] == "TEST":
        print("Running tests")
        pytest.main()

    print(multiple_of_3_and_5(1000))

if __name__ == "__main__":
    main()