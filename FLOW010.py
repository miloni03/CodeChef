# cook your dish here
t=int(input())
for i in range(t):
    x=input()
    if x=='b' or x=='B':
        print("BattleShip")
    elif x=='c' or x=='C':
        print("Cruiser")
    elif x=='d' or x=='D':
        print("Destroyer")
    elif x=='f' or x=='F':
        print("Frigate")