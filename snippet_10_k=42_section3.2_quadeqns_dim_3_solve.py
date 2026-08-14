#1.2 k = 42
#CODE
#--------------------
import sage.all
var('x, y')
eq1 = (x - 2544)*(y-1560*x + 2517732) == -6933526812*x - 231936*y - 88925764032
eq2 = (x - 2544)^2 -2^41 == -576*y + 785808*x-1172809472
print(f"===========================================================")
print(f"WEIGHT k=42")
print(f"===========================================================\n")

solutions = solve([eq1, eq2], x, y, solution_dict=True)
if solutions:
    for solution in solutions:
        x_approx = solution[x].n(digits=15)
        y_approx = solution[y].n(digits=15)
        print(f"Approximate solution (15 digits): x = {x_approx}, y = {y_approx}")
else:
    print("No solutions found.")
    