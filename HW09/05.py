import numpy as np

def pca(X, k):
    X = np.array(X, dtype=float)

    X_mean = X.mean(axis=0)
    X_centered = X - X_mean

    C = np.cov(X_centered, rowvar=False)

    eigvals, eigvecs = np.linalg.eig(C)
    idx = np.argsort(eigvals)[::-1]

    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]

    W = eigvecs[:, :k]
    Z = X_centered @ W

    return Z, eigvals[:k], W
