# cook your dish here
# Input: initial amount X and number of laddus N
X = int(input())  # Initial amount of money
N = int(input())  # Number of laddus bought

# Each laddu costs 10 and each jalebi costs 20
cost_laddu = 10
cost_jalebi = 20

# Calculate the remaining money after buying N laddus
remaining_money = X - (cost_laddu * N)

# Calculate how many jalebis can be bought with the remaining money
jalebis = remaining_money // cost_jalebi

# Output the number of jalebis
print(jalebis)
