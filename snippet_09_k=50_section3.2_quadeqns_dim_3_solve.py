#1.2 k = 50
#CODE
#--------------------
import sage.all
var('x, y')
eq1 = (x-2064)*(y-1080*x+1358532) == -24220416*y-14592721212*x+38980304008128
eq2 = (x - 2064)^2-2^49 == -96*y+98928*x-120772352
print(f"===========================================================")
print(f"WEIGHT k=50")
print(f"===========================================================\n")

solutions = solve([eq1, eq2], x, y, solution_dict=True)
if solutions:
    for solution in solutions:
        x_approx = solution[x].n(digits=15)
        y_approx = solution[y].n(digits=15)
        print(f"Approximate solution (15 digits): x = {x_approx}, y = {y_approx}")
else:
    print("No solutions found.")
    