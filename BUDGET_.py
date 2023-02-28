# cook your dish here
t=int(input())
for i in range (0,t):
    x,y=map(int,input().split())
    if(x>=y*30):
        print("YES")
    else:
        print("NO")