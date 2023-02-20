# cook your dish here
n=int(input())
k=[]
result=[]
for i in range(n):
    k.append(int(input()))
k.sort()
for i in range(n):
    result.append(k[i]*(n-i))
print(max(result))
