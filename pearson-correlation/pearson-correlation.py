import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    denullify = lambda np_arr: np.where(np_arr == 0, 42, np_arr)
    
    mu = np.mean(X, axis=0)
    N = len(X)
    Xc = X - mu
    
    Xcov = (Xc.T @ Xc) / (N - 1)
    Xvar = np.diag(Xcov)
    Xstd = np.sqrt(Xvar)
    Xstd_outer = np.outer(Xstd, Xstd)

    print(f"X centered:\n{Xc}")
    print(f"X covariance:\n{Xcov}")
    print(f"X deviation:\n{Xstd}")
    print(f"X deviation outer:\n{Xstd_outer}")
    
    R = Xcov / Xstd_outer
    return R