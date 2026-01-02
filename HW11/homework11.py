import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    """
    求解常係數齊次線性常微分方程 (ODE) 的通解。

    方程的一般形式為: a_n * y^(n) + a_{n-1} * y^(n-1) + ... + a_1 * y' + a_0 * y = 0
    其中 coefficients = [a_n, a_{n-1}, ..., a_0]。

    Args:
        coefficients (list or np.ndarray): ODE 的係數列表，從最高階項到零階項。

    Returns:
        str: ODE 的通解形式，例如 "y(x) = C_1e^(r1*x) + C_2e^(r2*x) + ... "。
    """
    if not coefficients or len(coefficients) == 0:
        return "係數列表不能為空。"

    roots = np.roots(coefficients)

    TOLERANCE = 1e-9

    root_multiplicity = {}

    processed_roots = set() 

    for root in roots:
        alpha = root.real
        beta = root.imag

        if abs(beta) < TOLERANCE:
            beta = 0.0
        if abs(alpha) < TOLERANCE:
            alpha = 0.0

        if beta == 0.0:
            r_key = alpha

            if r_key in processed_roots:
                continue

            count = sum(1 for r in roots if abs(r.real - alpha) < TOLERANCE and abs(r.imag) < TOLERANCE)
            root_multiplicity[r_key] = count
            processed_roots.add(r_key)
            
        else:
            if beta < 0:
                continue 

            r_key = (alpha, beta)

            if r_key in processed_roots:
                continue

            count = sum(1 for r in roots if abs(r.real - alpha) < TOLERANCE and abs(r.imag - beta) < TOLERANCE)

            root_multiplicity[r_key] = count

            processed_roots.add(r_key)

    solution_terms = []
    constant_index = 1 
    
    for root_key, multiplicity in root_multiplicity.items():
        if isinstance(root_key, float):
            r = root_key
            for k in range(multiplicity):
                term = f"C_{constant_index}"
                if k > 0:
                    term += f"x^{k}" if k > 1 else "x"
                term += f"e^({r}x)"
                solution_terms.append(term)
                constant_index += 1

        elif isinstance(root_key, tuple) and len(root_key) == 2:
            alpha, beta = root_key

            cos_terms = []
            for k in range(multiplicity):
                cos_term = f"C_{constant_index}"
                if k > 0:
                    cos_term += f"x^{k}" if k > 1 else "x"
                cos_terms.append(cos_term)
                constant_index += 1

            sin_terms = []
            for k in range(multiplicity):
                sin_term = f"C_{constant_index}"
                if k > 0:
                    sin_term += f"x^{k}" if k > 1 else "x"
                sin_terms.append(sin_term)
                constant_index += 1

            exp_term = f"e^({alpha}x)" if alpha != 0.0 else ""

            cos_part = " + ".join(cos_terms)
            sin_part = " + ".join(sin_terms)

            if exp_term:
                full_term = f"{exp_term}[({cos_part})cos({beta}x) + ({sin_part})sin({beta}x)]"
            else:
                full_term = f"({cos_part})cos({beta}x) + ({sin_part})sin({beta}x)"
                
            solution_terms.append(full_term)

    if not solution_terms:
        return "y(x) = 0 (可能係數錯誤或只有零解)"
    
    return "y(x) = " + " + ".join(solution_terms)

print("--- 實數單根範例 ---")
coeffs1 = [1, -3, 2]
print(f"方程係數: {coeffs1}")
print(solve_ode_general(coeffs1))

print("\n--- 實數重根範例 ---")
coeffs2 = [1, -4, 4]
print(f"方程係數: {coeffs2}")
print(solve_ode_general(coeffs2))

print("\n--- 複數共軛根範例 ---")
coeffs3 = [1, 0, 4]
print(f"方程係數: {coeffs3}")
print(solve_ode_general(coeffs3))

print("\n--- 複數重根範例 ---")
coeffs4 = [1, 0, 2, 0, 1]
print(f"方程係數: {coeffs4}")
print(solve_ode_general(coeffs4))

print("\n--- 高階重根範例 ---")
coeffs5 = [1, -6, 12, -8]
print(f"方程係數: {coeffs5}")
print(solve_ode_general(coeffs5))