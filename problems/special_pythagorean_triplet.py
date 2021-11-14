def pythagorean_triplet(s=1000):
    for i in range(0, (s + 1) // 2):
        for j in range(0, (s + 1) // 2):
            k = (i ** 2 + j ** 2) ** 0.5
            if i + j + k == s:
                return (i, j, int(k)), i * j * int(k)

    return (-1, -1, -1), -1

def main():
    print(pythagorean_triplet())

if __name__ == "__main__":
    main()