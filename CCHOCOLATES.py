# cook your dish here
t = int(input())
while t:
    x,y,z = map(int,input().split())
    a = 5*x + 10*y
    print(int(a/z))
    t = t -1