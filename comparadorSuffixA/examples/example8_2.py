def main():
    N = int(input())

    i = 0
    n = []
    for j in bin(N)[::-1]:
        if j == '1':
            n.append(2 ** i)
        i += 1

    print(len(n))
    for i in n:
        print(i)

main()
