# cook your dish here
# Input: initial amount X and number of laddus N
X = int(input()) 
N = int(input()) 

cost_laddu = 10
cost_jalebi = 20

remaining_money = X - (cost_laddu * N)

jalebis = remaining_money // cost_jalebi


print(jalebis)
