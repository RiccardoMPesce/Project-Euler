def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False 
        i += 1

    return True

def sum_primes(up=10):
    return sum([n for n in range(2, up) if is_prime(n)])

def main():
    print(sum_primes(2000000))

if __name__ == "__main__":
    main()