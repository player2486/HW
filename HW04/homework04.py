import random
import cmath

def poly_val(coef, x):
    y = 0
    for c in reversed(coef):
        y = y * x + c
    return y

def poly_derivative(coef):
    return [i * coef[i] for i in range(1, len(coef))]

def newton_root(coef, max_iter=1000, tol=1e-10):
    dcoef = poly_derivative(coef)

    x = complex(random.uniform(-1, 1), random.uniform(-1, 1))

    for _ in range(max_iter):
        fx = poly_val(coef, x)
        if abs(fx) < tol:
            return x

        dfx = poly_val(dcoef, x)
        if abs(dfx) < 1e-12:
            x += complex(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
            continue

        x = x - fx / dfx

    raise RuntimeError("牛頓法未收斂")

def deflate(coef, r):
    n = len(coef) - 1
    new_coef = [0] * n
    new_coef[-1] = coef[-1]

    for i in range(n - 2, -1, -1):
        new_coef[i] = coef[i + 1] + r * new_coef[i + 1]

    return new_coef

def root(coef):
    coef = coef[:]
    roots = []

    while len(coef) > 2:
        r = newton_root(coef)
        roots.append(r)
        coef = deflate(coef, r)

    c0, c1 = coef
    roots.append(-c0 / c1)

    return roots

if __name__ == "__main__":
    coef = [1, 0, 0, 0, 0, 1]  # x^5 + 1 = 0
    roots = root(coef)

    for r in roots:
        print(r)
