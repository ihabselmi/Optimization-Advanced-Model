
"Homework 12"
"Question 15.2.2"

# Import PULP and pandas library

from pulp import *
import pandas as pd


# Load data
mydata = pd.read_excel("/Users/ihabselmi/Desktop/Georgia Tech Classes/ISyE 6501/Week 12 - Optimization Advanced Models/Homework 12/diet.xls")

mydata = mydata[0:64].values.tolist()

# Store the vector into dict
foods = [x[0] for x in mydata]
cost = dict([(x[0], float(x[1])) for x in mydata])
calories = dict([(x[0], float(x[3])) for x in mydata])
chol = dict([(x[0], float(x[4])) for x in mydata])
fat = dict([(x[0], float(x[5])) for x in mydata])
sodium = dict([(x[0], float(x[6])) for x in mydata])
carbs = dict([(x[0], float(x[7])) for x in mydata])
fiber = dict([(x[0], float(x[8])) for x in mydata])
protein = dict([(x[0], float(x[9])) for x in mydata])
vitA = dict([(x[0], float(x[10])) for x in mydata])
vitC = dict([(x[0], float(x[11])) for x in mydata])
calcium = dict([(x[0], float(x[12])) for x in mydata])
iron = dict([(x[0], float(x[13])) for x in mydata])

# Our goal is to formulate an optimization model (a linear program) to find the cheapest 
# diet that satisfies the maximum and minimum daily nutrition constraints
# We create an LP Problem with parameter LpMinimize. This function will help us to save the problem.

problem_to_solve = LpProblem("Diet Optimization",LpMinimize)


food_picked = LpVariable.dicts("Foods", foods, lowBound = 0 )
chosen_food = LpVariable.dicts("Chosen", foods, lowBound = 0, upBound = 1, cat = "Binary")

# Below the objective function to minimize the cost
problem_to_solve += lpSum([cost[f]*food_picked[f] for f in foods]), "Total Cost"

# Below the constraints
'Calories range'
problem_to_solve += lpSum([calories[f]*food_picked[f] for f in foods]) >= 1500
problem_to_solve += lpSum([calories[f]*food_picked[f] for f in foods]) <= 2500 
'Cholesterol range'
problem_to_solve += lpSum([chol[f]*food_picked[f] for f in foods]) >= 30
problem_to_solve += lpSum([chol[f]*food_picked[f] for f in foods]) <= 240
'Total Fat range'
problem_to_solve += lpSum([fat[f]*food_picked[f] for f in foods]) >= 20
problem_to_solve += lpSum([fat[f]*food_picked[f] for f in foods]) <= 70 
'Sodium range'
problem_to_solve += lpSum([sodium[f]*food_picked[f] for f in foods]) >= 800
problem_to_solve += lpSum([sodium[f]*food_picked[f] for f in foods]) <= 2000
'Carbs range'
problem_to_solve += lpSum([carbs[f]*food_picked[f] for f in foods]) >= 130
problem_to_solve += lpSum([carbs[f]*food_picked[f] for f in foods]) <= 450
'Dietary Fiber range'
problem_to_solve += lpSum([fiber[f]*food_picked[f] for f in foods]) >= 125 
problem_to_solve += lpSum([fiber[f]*food_picked[f] for f in foods]) <= 250
'Protein range'
problem_to_solve += lpSum([protein[f]*food_picked[f] for f in foods]) >= 60
problem_to_solve += lpSum([protein[f]*food_picked[f] for f in foods]) <= 100
'Vitamines A range'
problem_to_solve += lpSum([vitA[f]*food_picked[f] for f in foods]) >= 1000
problem_to_solve += lpSum([vitA[f]*food_picked[f] for f in foods]) <= 10000
'Vitamines C range'
problem_to_solve += lpSum([vitC[f]*food_picked[f] for f in foods]) >= 400
problem_to_solve += lpSum([vitC[f]*food_picked[f] for f in foods]) <= 5000
'Calcium range'
problem_to_solve += lpSum([calcium[f]*food_picked[f] for f in foods]) >= 700
problem_to_solve += lpSum([calcium[f]*food_picked[f] for f in foods]) <= 1500
'Iron range'
problem_to_solve += lpSum([iron[f]*food_picked[f] for f in foods]) >= 10
problem_to_solve += lpSum([iron[f]*food_picked[f] for f in foods]) <= 40

# If a food is selected, then a minimum of 1/10 serving must be chosen.
for f in foods:
     problem_to_solve += food_picked[f] <= 10000000*chosen_food[f]
     problem_to_solve += food_picked[f] >= .1*chosen_food[f]

# Many people dislike celery and frozen broccoli. So at most one, but not both, can be selected.
problem_to_solve += chosen_food['Frozen Broccoli'] + chosen_food['Celery, Raw'] <=1

# To get day-to-day variety in protein, at least 3 kinds of meat/poultry/fish/eggs must be selected.
problem_to_solve += chosen_food['Tofu'] + chosen_food['Roasted Chicken'] + \
chosen_food['Poached Eggs']+chosen_food['Scrambled Eggs']+chosen_food['Bologna,Turkey'] \
+chosen_food['Frankfurter, Beef']+chosen_food['Ham,Sliced,Extralean'] \
+chosen_food['Kielbasa,Prk']+chosen_food['Hamburger W/Toppings'] \
+chosen_food['Hotdog, Plain']+chosen_food['Pork'] +chosen_food['Sardines in Oil'] \
+chosen_food['White Tuna in Water'] >= 3

# Print the output
print ("Solving Problem 15.2...............................")
problem_to_solve.solve()
print ("Status:", LpStatus[diet.status])
for v in problem_to_solve.variables():
    if v.varValue != 0.0: 
        print (v.name, "=", v.varValue)

print ("Total Cost of food with additiona constraints is $%.2f" % value(problem_to_solve.objective))