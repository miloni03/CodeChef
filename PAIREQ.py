# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    max_count = 0
    i = 0
    while i<n:
        c = arr.count(arr[i])
        if c > max_count:
            max_count = c
        i = i + c
        
    print(n - max_count)