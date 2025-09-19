import cmath

def root2(a, b, c):
    D = b**2 - 4*a*c
    r1 = (-b + cmath.sqrt(D)) / (2*a)
    r2 = (-b - cmath.sqrt(D)) / (2*a)
    
    print(a*r1**2 + b*r1 + c)
    print(a*r2**2 + b*r2 + c)
    return r1, r2

print(root2(1, -3, 2))
print(root2(1, 1, 1))
