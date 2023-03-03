# cook your dish here
t=int(input())
for i in range(t):
    c1=0
    c2=0
    n=int(input())
    x=list(map(str,input().split()))
    for i in range(n):
        if x[i]=="START38":
            c1=c1+1
        if x[i]=="LTIME108":
            c2=c2+1
    print(c1,c2)