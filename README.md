# Optimization-Advanced-Model
In the videos, we saw the “diet problem”. (The diet problem is one of the first large-scale optimization problems to be studied in practice. Back in the 1930’s and 40’s, the Army wanted to meet the nutritional requirements of its soldiers while minimizing the cost.) In this homework you get to solve a diet problem with real data. The data is given in the file diet.xls.
1. Formulate an optimization model (a linear program) to find the cheapest diet that satisfies the maximum and minimum daily nutrition constraints, and solve it using PuLP. Turn in your code and the solution. (The optimal solution should be a diet of air-popped popcorn, poached eggs, oranges, raw iceberg lettuce, raw celery, and frozen broccoli. UGH!)
2. Please add to your model the following constraints (which might require adding more variables) and solve the new model:
a. If a food is selected, then a minimum of 1/10 serving must be chosen. (Hint: now you will
need two variables for each food i: whether it is chosen, and how much is part of the diet.
You’ll also need to write a constraint to link them.)
b. Many people dislike celery and frozen broccoli. So at most one, but not both, can be
selected.
c. To get day-to-day variety in protein, at least 3 kinds of meat/poultry/fish/eggs must be
selected. [If something is ambiguous (e.g., should bean-and-bacon soup be considered meat?), just call it whatever you think is appropriate – I want you to learn how to write this type of constraint, but I don’t really care whether we agree on how to classify foods!]
