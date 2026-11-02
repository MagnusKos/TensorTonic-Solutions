import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    rows_num = len(seqs)

    if not rows_num:
        return np.empty((0,0), dtype=int)

    cols_num = max(len(seq) for seq in seqs) if max_len is None else max_len
    seqs_processed = []
    
    for row in seqs:
        if len(row) < cols_num:
            seqs_processed.append(list(row) + [pad_value] * (cols_num - len(row)))
        else:
            seqs_processed.append(list(row[:cols_num]))

    return np.asarray(seqs_processed)