# cook your dish here
t= int(input())
for i in range(t):
    x, y= map(int,input().split())
    if 15*x - 2*y >= 0 :
        print("YES")
    else:
        print("NO")