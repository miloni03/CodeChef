# cook your dish here
for t in range(int(input())):
    n,k = map(int,input().split())
    if k != 0:
        print(n%k)
    else:
        print(n)