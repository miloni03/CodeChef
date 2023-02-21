n=int(input())
x=list(map(int,input().split()))
x.sort()
p=0
s=0
for i in range(0,n,2):
    p += 1
    s += (n-1-i)*(x[n-p]-x[p-1])
print(s)