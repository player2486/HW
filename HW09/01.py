import numpy as np

def det_recursive(A):
    A = np.array(A, dtype=float)
    n = A.shape[0]

    if n == 1:
        return A[0, 0]

    if n == 2:
        return A[0,0]*A[1,1] - A[0,1]*A[1,0]

    det = 0.0
    for j in range(n):
        sub = np.delete(np.delete(A, 0, axis=0), j, axis=1)
        det += ((-1)**j) * A[0, j] * det_recursive(sub)

    return det
