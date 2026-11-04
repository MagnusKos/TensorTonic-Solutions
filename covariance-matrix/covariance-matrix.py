import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    mu = np.mean(X, axis=0)
    Xc = X - mu
    N = len(X)
    Sigma = (Xc.T @ Xc) / (N - 1)
    return Sigma