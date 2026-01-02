import cmath

def root3(a, b, c, d):
    if a == 0:
        raise ValueError("a 不可為 0")

    p = (3*a*c - b*b) / (3*a*a)
    q = (2*b**3 - 9*a*b*c + 27*a*a*d) / (27*a**3)

    delta = (q/2)**2 + (p/3)**3
    sqrt_delta = cmath.sqrt(delta)

    u = (-q/2 + sqrt_delta) ** (1/3)
    v = (-q/2 - sqrt_delta) ** (1/3)

    omega = complex(-0.5, cmath.sqrt(3)/2)
    omega2 = complex(-0.5, -cmath.sqrt(3)/2)

    t1 = u + v
    t2 = omega*u + omega2*v
    t3 = omega2*u + omega*v

    shift = b / (3*a)

    return (
        t1 - shift,
        t2 - shift,
        t3 - shift
    )


# ===== 主程式（一定要有，否則不會顯示）=====
if __name__ == "__main__":
    roots = root3(1, 0, 0, 1)  # x^3 + 1 = 0
    for r in roots:
        print(r)
