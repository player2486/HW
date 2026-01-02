import numpy as np

def lu_decomposition(A):
    A = np.array(A, dtype=float)
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        # 計算 U 的第 i 列
        for j in range(i, n):
            U[i, j] = A[i, j] - np.sum(L[i, :i] * U[:i, j])

        # 計算 L 的第 i 欄
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.sum(L[j, :i] * U[:i, i])) / U[i, i]

    return L, U


def det_via_lu(A):
    _, U = lu_decomposition(A)
    return np.prod(np.diag(U))
