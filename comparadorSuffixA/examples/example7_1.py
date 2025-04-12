import sys

def solve():
    N = int(input())
    p = 8
    ans = []

    while p > 0:
        if N - p >= 0:
            ans.append(p)
            N -= p
        p //= 2

    print(len(ans))
    print(*ans, sep='\n')

if __name__ == '__main__':
    solve()