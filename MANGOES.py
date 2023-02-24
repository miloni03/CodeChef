# cook your dish here
T=int(input())
for i in range(T):
   X,Y,Z=map(int,input().split())
   a=(Z-Y)/X
   print(int(a))