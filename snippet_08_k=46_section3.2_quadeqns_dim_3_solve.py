#1.2 k = 46
#CODE
#--------------------
import sage.all
var('x, y')
eq1 = (x-2304)*(y-1320*x+1909332) == 3844224*y-32589636012*x+51927428533248
eq2 = (x - 2304)^2-2^45 == -336*y+413568*x-574042112
print(f"===========================================================")
print(f"WEIGHT k=46")
print(f"===========================================================\n")

solutions = solve([eq1, eq2], x, y, solution_dict=True)
if solutions:
    for solution in solutions:
        x_approx = solution[x].n(digits=15)
        y_approx = solution[y].n(digits=15)
        print(f"Approximate solution (15 digits): x = {x_approx}, y = {y_approx}")
else:
    print("No solutions found.")
    