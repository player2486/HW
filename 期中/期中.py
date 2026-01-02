"""
數值積分範例程式
使用梯形法與辛普森法計算定積分
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) 

def trapezoidal_rule(f, a, b, n):
    """
    f: 函數
    a: 積分下限
    b: 積分上限
    n: 分割小區間數
    """
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = (h/2) * (y[0] + 2*np.sum(y[1:-1]) + y[-1])
    return integral

def simpson_rule(f, a, b, n):
    """
    n 必須是偶數
    """
    if n % 2 == 1:
        n += 1
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = (h/3) * (y[0] + 2*np.sum(y[2:n:2]) + 4*np.sum(y[1:n:2]) + y[n])
    return integral

if __name__ == "__main__":
    a = 0 
    b = np.pi 
    n = 100 

    I_trap = trapezoidal_rule(f, a, b, n)
    I_simp = simpson_rule(f, a, b, n)
    I_exact = 2 

    print(f"梯形法積分結果: {I_trap}")
    print(f"辛普森法積分結果: {I_simp}")
    print(f"精確值: {I_exact}")
    print(f"梯形法誤差: {abs(I_trap - I_exact)}")
    print(f"辛普森法誤差: {abs(I_simp - I_exact)}")

    x_vals = np.linspace(a, b, 1000)
    y_vals = f(x_vals)

    plt.figure(figsize=(8,4))
    plt.plot(x_vals, y_vals, label='f(x) = sin(x)')
    plt.fill_between(x_vals, 0, y_vals, color='skyblue', alpha=0.4)
    plt.title("數值積分示意圖")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
