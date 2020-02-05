"Homework 12"
"Question 15.2.1"

# Import PULP and pandas library

from pulp import *
import pandas as pd


# Load data

mydata = pd.read_excel("/Users/ihabselmi/Desktop/Georgia Tech Classes/ISyE 6501/Week 12 - Optimization Advanced Models/Homework 12/diet.xls")

# Let's convert the data into list because we will use python dict
diet_data = mydata[0:64] 
diet_data = diet_data.values.tolist()


# Set up the maximum and minimum daily nutrition constraints
minimum_daily_nutrition = mydata[65:66].values.tolist() 
maximum_daily_nutrition = mydata[66:67].values.tolist()
   


# Let's extract vector from the data using the python "dict" structure

foods = [j[0] for j in diet_data] #list of food names

cost = dict([(j[0], float(j[1])) for j in diet_data]) # cost for each food

nutrients = []
for i in range(0,11): # for loop running through each nutrient: 11 times starting with 0
    nutrients.append(dict([(j[0], float(j[i+3])) for j in diet_data])) # amount of nutrient i in food j


# Our goal is to formulate an optimization model (a linear program) to find the cheapest 
# diet that satisfies the maximum and minimum daily nutrition constraints
# We create an LP Problem with parameter LpMinimize. This function will help us to save the problem.

problem_to_solve = LpProblem('Food optimization', LpMinimize) 


# We define the variables that the lower limit for each food is 0 as we cannot eat neagtive amount of food

food_picked = LpVariable.dicts("Foods", foods, 0)

# Below the objective function

problem_to_solve += lpSum([cost[f] * food_picked[f] for f in foods]), 'Total Cost'


# The two constraints are added to 'prob' which are the maximum and minimum daily nutrition constraints
nutrient_variables = list(mydata.columns.values) 

for i in range(0,11):
    problem_to_solve += lpSum([nutrients[i][j] * food_picked[j] for j in foods]) >= minimum_daily_nutrition[0][i+3], 'min nutrient ' + nutrient_variables[i]
    problem_to_solve += lpSum([nutrients[i][j] * food_picked[j] for j in foods]) <= maximum_daily_nutrition[0][i+3], 'max nutrient ' + nutrient_variables[i]


# Solve the diet problem

problem_to_solve.solve()


# Print the output

print()
print("---------The solution to the diet problem is----------")
for var in problem_to_solve.variables():
    if var.varValue > 0:
        print(str(var.varValue)+" serving size "+str(var).replace('Foods_','') )
print()
print("Total cost = $%.2f" % value(problem_to_solve.objective))        

        





