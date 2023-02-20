# cook your dish here
n=list(map(int,input().split(" ")))
stack=list(map(int,input().split(" ")))
oper=list(map(int,input().split(" ")))
index=0
crane=0
for i in oper:
    if i==0:
        break
    elif i==1:
        if index==0:
            pass
        else:
            index-=1
    elif i==2:
        if index==n[0]-1:
            pass
        else:
            index+=1
    elif i==3:
        if crane==0 and stack[index]!=0:
            stack[index]-=1
            crane=1
    elif i==4:
        if crane==1 and stack[index]<n[1]:
            stack[index]+=1
            crane=0
print(*stack)