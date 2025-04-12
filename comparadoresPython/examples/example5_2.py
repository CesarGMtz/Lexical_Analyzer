n,m = map(int,input().split())
ar = [0]*(m+2)
sm = 0
for _ in range(n):
    l,r,s = map(int,input().split())
    ar[l] += s
    ar[r+1] -= s
    sm += s
for i in range(m+1):
    ar[i+1] += ar[i]
print(sm-min(ar[1:m+1]))
