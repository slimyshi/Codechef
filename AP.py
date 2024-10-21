# arthimetic
for _ in range(int(input())):
    X,Y,Z = map(int, input().split())
    if Y-X == Z-Y:
        print(0)
    else:
        print(1)