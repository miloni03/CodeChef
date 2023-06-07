# cook your dish here
for t in range(int(input())):
    abc = list(map(int, input().split()))
    abc.sort()
    print("Yes" if abc[2] == abc[0] + abc[1] else "No")