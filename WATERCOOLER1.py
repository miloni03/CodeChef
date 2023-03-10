# cook your dish here
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    d=a*c
    if(d<b):
        print("YES")
    else:
        print("NO")