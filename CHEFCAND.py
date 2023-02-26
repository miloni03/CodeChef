# cook your dish here
for t in range(int(input())):
    n,x=map(int,input().split())
    if n<x:
        print("0")
        continue
    n=n-x
    if n%4==0:
        print(n//4)
    else:
        print((n//4)+1)
    