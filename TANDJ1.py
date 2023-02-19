# cook your dish here
T = int(input())
for i in range(T):
    a,b,c,d,K = map(int,input().split())
    steps = abs(c-a)+abs(d-b)
    if steps==K:
        print("Yes")
    elif K>steps and (K-steps)%2==0:
        print("Yes")
    else:
        print("No")