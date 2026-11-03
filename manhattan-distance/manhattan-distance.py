import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    vec = np.asarray((x,y))
    dist_l1 = np.sum(np.abs(np.diff(vec, axis=0)), axis=1, dtype=float)[0]
    return dist_l1