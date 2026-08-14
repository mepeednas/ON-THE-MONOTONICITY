#1.2 k = 40
#CODE
#--------------------
import sage.all
var('x, y')
eq1 = (x - 1800)*(y-816*x + 1019764) == 1593543564*x + 392832*y + 11401818279840
eq2 = (x-1800)^2 -2^(39) == 168*y + 18936*x-90399680
print(f"===========================================================")
print(f"WEIGHT k=40")
print(f"===========================================================\n")

solutions = solve([eq1, eq2], x, y, solution_dict=True)
if solutions:
    for solution in solutions:
        x_approx = solution[x].n(digits=15)
        y_approx = solution[y].n(digits=15)
        print(f"Approximate solution (15 digits): x = {x_approx}, y = {y_approx}")
else:
    print("No solutions found.")