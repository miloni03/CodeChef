# cook your dish here
t=int(input())
for i in range(t):
    na,nb,nc=map(int,input().split())
    if na>nb:
        if na>nc:
            if na>nb+nc:
                print("YES")
            else:
                print("NO")
        else:
            if nc>na+nb:
                print("YES")
            else:
                print("NO")
    else:
        if nb>nc:
            if nb>na+nc:
                print("YES")
            else:
                print("NO")
        else:
            if nc>na+nb:
                print("YES")
            else:
                print("NO")
            
        