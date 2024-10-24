# cook your dish here
import string
name= list(string.ascii_lowercase)
for i in range(int(input())):
    x, y = map(int, input().split(" "))
    a = list(str((input())))
    b = list(str((input())))
    c = a+b
    meow = list(set(name)^set(c))
    if len(set(meow))== 0:
        print("NO")
    else:
        print("YES")