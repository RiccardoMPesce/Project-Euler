def get_nth_prime(n):
    primes = [1]

    i = 2
    while len(primes) < n + 1:
        is_prime = True 
        for j in primes:
            if i % j == 0 and j != 1:
                is_prime = False 
            
        if is_prime:
            primes += [i]

        i += 1

    return primes[n]

def main():
    print(get_nth_prime(10001))

if __name__ == "__main__":
    main()