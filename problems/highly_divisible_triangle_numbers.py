def generate_list_of_triangle_numbers(up_to_n):
    ls = []
    
    for i in range(1, up_to_n + 1):
        sum = i
        for j in range(1, i):
            sum += j
        ls += [sum]
    
    return ls


def is_triangle_number(n):
    s = 0
    i = 1

    while s < n:
        s += i
        i += 1

    return s == n


def divide_and_return_n_divisors(n, tab={}):
    tab[n] = [n]

    for i in range(1, n):
        if n % i == 0:
            tab[n] += [div for div in tab[i] if div not in tab[n]]

    return tab


def main():
    i = 0
    d = 0
    tab = {}
    
    while d < 5000:
        i += 1
        tab = divide_and_return_n_divisors(i, tab)
        if is_triangle_number(i):
            print(f"Number {i} has {len(tab[i])} divisors")

    print(f"Finally, number {i} has {d} divisors")

if __name__ == "__main__":
    main()