import sys
N=int(input())
a,b=map(int,input().split())
K=int(input())
P=list(map(int,input().split()))
s=set()
s.add(a)
s.add(b)
for i in range(K):
  if P[i] in s:
    print("NO")
    sys.exit()
  s.add(P[i])
print("YES")