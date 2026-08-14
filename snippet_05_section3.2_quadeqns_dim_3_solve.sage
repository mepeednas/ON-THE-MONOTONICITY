#For solve() demonstration, use this code
var('x, y')
eq1 = (x - 2040)*(-1056*x + y + 1506204) == -12*(11640243*x + 4544*y - 500135144040)
eq2 = (x - 2040)^2-2^(35) == -72*y+270216*x-447488960
print(f"This program hardcodes the equations a_f(2)a_f(3)= a_f(6) and a_f(2)^2 - 2^(k-1) = a_f(4) for k=36 and provides a computer generated solution")
print(f"by using the solve function in sagemath which may use algebraic/numerical solvers to arrive at all the common solutions.")
print(f"Accordingly, the second(x) and third coordinates(y) of each f with respect to Victor-Mille basis is displayed.\n")
solutions = solve([eq1, eq2], x, y, solution_dict=True)
if solutions:
    for solution in solutions:
        x_approx = solution[x].n(digits=15)
        y_approx = solution[y].n(digits=15)
        print(f"Approximate solution (15 digits): x = {x_approx}, y = {y_approx}\n")
else:
    print("No solutions found.\n")
print(f"It can be observed that there is a solution (x,y) whose each component is positive and thus k=36 is a good weight.")
