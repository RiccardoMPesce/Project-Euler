def multiple_of_3_and_5(limit, test=False) -> int:
    """
    Given limit as an integer, returns the sum of all the multiple of
    3 or 5 or both less than limit
    """
    return sum([i for i in range(limit) if i % 3 == 0 or i % 5 == 0])