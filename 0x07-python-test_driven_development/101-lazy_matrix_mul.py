import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        list: Resulting matrix after multiplication.

    Raises:
        ValueError: If the matrices cannot be multiplied.

    """
    try:
        result = np.dot(m_a, m_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
