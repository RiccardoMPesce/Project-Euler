def prime_factor_finder(n):
    factors = []
    last_div = 1
    found = False

    while n > 1:
        for i in range(last_div + 1, n):
            if n % i == 0:
                found = True
                factors += [i]
                n //= i
                last_div = i
                break
        if found:
            found = False 
        else:
            break

    return n

def main():
    print(prime_factor_finder(600851475143))

if __name__ == "__main__":
    main()