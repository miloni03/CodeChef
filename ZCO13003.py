# cook your dish here
N, K = map(int, input().split())
Q = list(map(int, input().split()))
Q.sort()
j = N-1
i = 0
c = 0
while j>i:
    if Q[j]+Q[i] < K:
        c += (j-i)
        i+=1
    else:
        j-=1
print(c)