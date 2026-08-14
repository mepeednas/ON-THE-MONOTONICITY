# This is a common program suitable for performing operations O1-O4 for dimension 3 cases only. 
# Give the desired weight k in the range 36,40,42,44,46,50 as input argument for the function analyze_weight() in the last line of the code
# Run it in https://sagecell.sagemath.org/ or any suitable interfaces like cocalc to obtain the desired output and to verify the
# equations obtained in the manuscript "ON THE MONOTONICITY OF HECKE L-FUNCTIONS AND THE VICTOR-MILLER BASIS"

def analyze_weight(k):
    # 1. Setup the basic modular forms (Prec=8 to safely get up to q^6)
    prec = 8
    Delta = delta_qexp(prec)
    # Multiply to ensure the constant term a(0) = 1
    E4 = 240 * eisenstein_series_qexp(4, prec)
    E6 = -504 * eisenstein_series_qexp(6, prec)

    # 2. Match k to its Victor-Miller basis elements for d=3
    if k == 36:
        v3, v2, v1 = Delta^3, Delta^2 * E6^2, Delta * E6^4
    elif k == 40:
        v3, v2, v1 = Delta^3 * E4, Delta^2 * E6^2 * E4, Delta * E6^4 * E4
    elif k == 42:
        v3, v2, v1 = Delta^3 * E6, Delta^2 * E6^3, Delta * E6^5
    elif k == 44:
        v3, v2, v1 = Delta^3 * E4^2, Delta^2 * E6^2 * E4^2, Delta * E6^4 * E4^2
    elif k == 46:
        v3, v2, v1 = Delta^3 * E6 * E4, Delta^2 * E6^3 * E4, Delta * E6^5 * E4
    elif k == 50:
        v3, v2, v1 = Delta^3 * E6 * E4^2, Delta^2 * E6^3 * E4^2, Delta * E6^5 * E4^2
    else:
        print("Weight not supported or dimension is not 3.")
        return

    # 3. Extract the integer coefficients of v_j^k 
    b1_2, b1_3, b1_4, b1_6 = ZZ(v1[2]), ZZ(v1[3]), ZZ(v1[4]), ZZ(v1[6])
    b2_2, b2_3, b2_4, b2_6 = ZZ(v2[2]), ZZ(v2[3]), ZZ(v2[4]), ZZ(v2[6])
    b3_2, b3_3, b3_4, b3_6 = ZZ(v3[2]), ZZ(v3[3]), ZZ(v3[4]), ZZ(v3[6])

    # 4. Perform (O1): Calculate constants C1, C2, C3
    C1 = -b2_3*(b2_4 - b1_2) - b1_3 + b2_6
    C2 = b1_6 - b1_2*b1_3 - b2_3*b1_4 + b2_3*(b1_2)^2 - (2^(k-1))*b2_3
    C3 = b1_2 - b3_6 + b2_3*b3_4

    # 5. Perform (O2): Obtain linear relation in y
    x, y = var('x y')
    O2_LHS_y_coeff = x + b1_2 - b3_6
    O2_RHS = b1_6 + x*b2_6 - (x + b1_2)*(b2_3*x + b1_3)

    # 6. Perform (O3): Isolate y from Eq 2 of system I
    O3_num = (x + b1_2)^2 - x*b2_4 - b1_4 - 2^(k-1)
    O3_den = b3_4
    # Note: y = O3_num / O3_den

    # 7. Perform (O4): Substitute (O3) into (O2) to get Cubic Polynomial
    # (O2_LHS_y_coeff) * (O3_num / b3_4) = O2_RHS
    # Multiply entire equation by b3_4 to clear denominator and keep integer coeffs
    cubic_poly = (O2_LHS_y_coeff * O3_num) - (b3_4 * O2_RHS)

    # Results
    print(f"This program takes weight k as input and uses two Hecke relations a_f(2)a_f(3)= a_f(6) and a_f(2)^2 - 2^(k-1) = a_f(4)")
    print(f"to generate a system of two non-linear equations in x and y variables(defined in manuscript) and perform the operations O1-O4 on them")
    print(f" as described in the manuscript ON THE MONOTONICITY OF HECKE L-FUNCTIONS AND THE VICTOR-MILLER BASIS.\n")
    print(f"Please change the value of k as per your requirement at the end of the code\n")
    print(f"===========================================================")
    print(f"   ALGEBRAIC OPERATIONS FOR WEIGHT k = {k}")
    print(f"===========================================================\n")

    print(f"--- (O1) Rational expression for y ---")
    print(f"y = ({C1} * x + {C2}) / (x + {C3})\n")

    print(f"--- (O2) Grouped a_f(2)a_f(3)= a_f(6) so as to isolate y ---")
    print(f"({O2_LHS_y_coeff.expand()}) * y = {O2_RHS.expand()}\n")

    print(f"--- (O3) Expression isolating y from a_f(2)^2 - 2^(k-1) = a_f(4) ---")
    print(f"y = ({O3_num.expand()}) / {O3_den}\n")

    print(f"--- (O4) Monic Cubic Polynomial p(x) = 0 ---")
    print(f"p(x) = {cubic_poly.expand()} = 0\n")


# Change this value to 36, 40, 42, 44, 46, or 50 to see the desired result!
analyze_weight(36)
