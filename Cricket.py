# cook your dish here
from math import comb
t=int(input())
for i in range(t):
    n=int(input())
    p= 2*(comb(n, 2))
    print(p)