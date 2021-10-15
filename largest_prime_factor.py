def prime_factor_finder(n):
    factors = []

    last_div = 1
    while n > 1:
        for i in range(last_div, n):
            if n % i == 0:
                factors += [i]
                n //= i
                last_div = i + 1
                break
        print(f"n is {n}")

    return factors

def main():
    print(prime_factor_finder(600851475143))

if __name__ == "__main__":
    main()