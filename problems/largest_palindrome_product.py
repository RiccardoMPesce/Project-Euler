def largest_palindrome_product(digits=3):
    top = (10 ** digits)
    bottom = 10 ** (digits - 1)
    palindromes = []

    for i in range(bottom, top):
        for j in range(bottom, top):
            if str(i * j) == str(i * j)[::-1]:
                palindromes.append(i * j)

    return max(palindromes)

def main():
    print(largest_palindrome_product())

if __name__ == "__main__":
    main()