def sum_square_difference(n):
    return sum([i for i in range(1, n + 1)]) ** 2 - sum([i ** 2 for i in range(1, n + 1)])

def main():
    n = 10
    print(sum_square_difference(100))

if __name__ == "__main__":
    main()