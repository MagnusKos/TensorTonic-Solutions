import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    rows_num = len(A)
    cols_num = len(A[0])

    A_t_cheaty = np.column_stack(A)  # technically speaking, this is not a transposing =)
    return A_t_cheaty
    pass
