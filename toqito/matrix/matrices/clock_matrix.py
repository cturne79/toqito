"""Generates the clock matrix."""
from cmath import exp, pi
import numpy as np


def clock_matrix(dim: int) -> np.ndarray:
    """
    Produces a clock matrix.
    :param dim: Dimension of the matrix.

    Returns the clock matrix of dimension DIM described in [1].

    The clock matrix generates the following DIM x DIM matrix

    Sigma_1 = [[1 0 0 ... 0],
               [0 w ... 0],
               [0 0 w^2 ... 0],
               [. ... . ],
               [0 0 0 ... w^(d-1)]]

    where w is the n-th primitive root of unity.

    References:
    [1] Wikipedia: Generalizations of Pauli matrices
        (https://en.wikipedia.org/wiki/Generalizations_of_Pauli_matrices).
    """
    c_var = 2j * pi / dim
    omega = (exp(k * c_var) for k in range(dim))
    return np.diag(list(omega))
