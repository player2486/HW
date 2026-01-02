import numpy as np

def svd_from_eig(A):
    A = np.array(A, dtype=float)
    ATA = A.T @ A

    eigvals, V = np.linalg.eig(ATA)
    idx = np.argsort(eigvals)[::-1]

    eigvals = eigvals[idx]
    V = V[:, idx]

    Sigma = np.diag(np.sqrt(eigvals))
    U = A @ V @ np.linalg.inv(Sigma)

    return U, Sigma, V.T
