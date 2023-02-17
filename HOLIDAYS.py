# cook your dish here
def solve():
    n, w = map(int, input().split())
    l = sorted(list(map(int, input().split())))
    x = 0
    for j in range(n-1, -1, -1):
        x += l[j]
        if x >= w: return j
    return 0
    
    
for i in range(int(input())):
    print(solve())