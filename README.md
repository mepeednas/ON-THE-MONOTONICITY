README for Computational Supplements
----------------------------------------
This repository contains the SageMath scripts used to extract the Fourier coefficients and verify the algebraic eliminations in the paper "On the Monotonicity of Hecke L-Functions and the Victor Miller Basis".

snippet_01_section3.1_Fourier_dim_2.py: Generates the exact Fourier coefficients for the Victor-Miller basis elements for d=2.

snippet_02_section3.1_rearranged_quadeqns_dim_2.py: Generates the quadratic equations for d=2.

snippet_03_section3.2_Fourier_dim_3.py: Generates the exact Fourier coefficients for the Victor-Miller basis elements for d=3.

snippet_04_section3.2_quadeqns_dim_3.py: Performs the exact algebraic operations (O1-O4) to generate the cubic polynomials for any weight k where \dim S_k=3.

snippet_05-snippet_10: Uses SageMath's internal solvers to numerically verify the exact roots of the cubic polynomials for weights 36, 40, 42, 44, 46, and 50.
