import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    rng = np.random.default_rng(seed)
    
    x_mu = np.mean(x)
    x_N = len(x)
    a = (1 - ci) / 2
    quantiles = [a, 1 - a]

    """
    Create index matrix. Each row is exactly of input's 'x' length,
    and we'll have n_bootstrap rows in total.
    """
    xb_idx_mat = rng.integers(0, x_N, (n_bootstrap, x_N))
    xb_mat = np.asarray(x)[xb_idx_mat]  # Advanced indexing in Numpy
    xb_mu_vec = np.sort(np.mean(xb_mat, axis=1))  # sort is not needed for np.quantile, but just in case
    xb_mu = np.mean(xb_mu_vec)
    xb_quantiles = np.quantile(xb_mu_vec, quantiles)

    output = {
        "bootstrap_mean": xb_mu,
        "lower": xb_quantiles[0],
        "upper": xb_quantiles[1]
    }
    
    print(f"{x_mu}, {xb_mu}, {xb_quantiles}")
    return output