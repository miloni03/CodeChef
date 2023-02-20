# cook your dish here
n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
x,y = 0, 0
counter = 0
while y < n:
    if l[y] - l[x] >= k:
        x += 1
        counter += n - y
    else:
        y += 1

print(counter)