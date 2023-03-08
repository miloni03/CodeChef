# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=x/y
    if a%2==0:
        print("Yes")
    else:
        print("No")
    