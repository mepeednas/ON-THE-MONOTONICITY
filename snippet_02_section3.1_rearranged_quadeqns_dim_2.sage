#This program displays the simplified quadratic equation satisfied by x variable for each case of S_k whose dimension is 2
print(f"This program displays the simplified quadratic equation satisfied by x variable for each case of S_k whose dimension is 2\n")
#k=24
x = var('x')
eq = (x - 1032)*(-48*x + 245196) == 143820*x - 1130921568
final_eq = (eq.lhs() - eq.rhs()).expand() == 0
print(f"The rearranged quad eqn for k=24 is: {final_eq}\n")
#k=28
eq = (x-792)*(192*x-324) == -1438020*x+38626945632
final_eq = (eq.lhs() - eq.rhs()).expand() == 0
print(f"The rearranged quad eqn for k=28 is: {final_eq}\n")
#k=30
eq = (x-1536)*(-552*x+748692) == -4868460*x - 243444676608
final_eq = (eq.lhs() - eq.rhs()).expand() == 0
print(f"The rearranged quad eqn for k=30 is: {final_eq}\n")
#k=32
eq = (x-552)*(432*x - 188244) == 17312940*x + 956114464032
final_eq = (eq.lhs() - eq.rhs()).expand() == 0
print(f"The rearranged quad eqn for k=32 is: {final_eq}\n")
#k=34
eq = (x-1296)*(-312*x+382212) == 37942020*x-2705241457728
final_eq = (eq.lhs() - eq.rhs()).expand() == 0
print(f"The rearranged quad eqn for k=34 is: {final_eq}\n")
#k=38
eq = (x-1056)*(-72*x+73332) == 13994100*x-9907823173248
final_eq = (eq.lhs() - eq.rhs()).expand() == 0
print(f"The rearranged quad eqn for k=38 is: {final_eq}\n")
