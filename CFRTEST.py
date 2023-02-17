# cook your dish here
for _ in range(int(input())):
    n = int(input())
    
    lit = list(map(int, input().split()))
    lit = set(lit)
    
    print(len(lit))