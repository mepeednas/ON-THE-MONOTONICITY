#1.2 k = 44
#CODE
#--------------------
import sage.all
var('x, y')
eq1 = (x - 1560)*(y - 576*x + 588924) == 17804242044*x - 2270208*y - 7427777565600
eq2 = (x - 1560)^2-2^43 == -174744*x + 408*y + 150222400
print(f"===========================================================")
print(f"WEIGHT k=44")
print(f"===========================================================\n")

solutions = solve([eq1, eq2], x, y, solution_dict=True)
if solutions:
    for solution in solutions:
        x_approx = solution[x].n(digits=15)
        y_approx = solution[y].n(digits=15)
        print(f"Approximate solution (15 digits): x = {x_approx}, y = {y_approx}")
else:
    print("No solutions found.")
    
