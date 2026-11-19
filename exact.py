import numpy as np


def exact_ground_energy(hamiltonian):
    """
    Calculate the exact ground-state energy
    by diagonalizing the Hamiltonian.

    Args:
        hamiltonian: Qiskit SparsePauliOp

    Returns:
        float: Ground-state energy
    """
    H_matrix = hamiltonian.to_matrix()

    # Hamiltonian should be hermitian, so can use more efficient eigenvalue solver
    if not np.allclose(H_matrix, H_matrix.conj().T):
        raise ValueError("Hamiltonian must be Hermitian")

    eigenvalues = np.linalg.eigvalsh(H_matrix)
    return float(eigenvalues[0])
