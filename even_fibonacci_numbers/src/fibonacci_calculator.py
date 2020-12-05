def fibonacci_calculator(n : int) -> list:
    """
    Calculate the first n elements of the Fibonacci sequence
    """
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        seq = [1, 2]
        i = 3
        while i <= n:
            seq.append(seq[-2] + seq[-1])
            i += 1
        return seq
