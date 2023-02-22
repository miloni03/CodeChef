# cook your dish here
t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().split()))
    if(a >= b and a <= c):
        print("Take second dose now")
    elif(a < b):
        print("Too Early")
    elif(a > c):
        print("Too Late")
    