# cook your dish here
n = int(input())
x=list(map(int, input().split()))
c=x[:3]
for i in range(3,n):
    s=min(c[-3:])+x[i]
    c.append(s)
print(min(c[-3:]))