# cook your dish here
t=int(input())
for i in range(t):
    a,c=(map(int,input().split()))
    d=(a+c)//2
    e=a+c
    if e%2==0:
        print(d)
    else:
        print(-1)