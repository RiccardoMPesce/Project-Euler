import py
def multiple_of_3_and_5(limit, test=False) -> int:
    """
    
    """
    return sum([i for i in range(limit) if i % 3 == 0 or i % 5 == 0])