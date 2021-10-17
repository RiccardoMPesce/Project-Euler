def smallest_multiple(n=10):
    high = 1 

    for i in range(1, n + 1):
        high *= i
    
    for i in range(n, high + 1, n):
        # Assuming we found the number we're loking for
        found = True
        for j in range(1, n + 1):
            if i % j != 0:
                found = False 
        if found:
            return i

    return high

def main():
    print(smallest_multiple(20))

if __name__ == "__main__":
    main()