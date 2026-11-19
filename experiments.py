import numpy as np

from hamiltonian import build_hamiltonian
from ansatz import build_ansatz
from exact import exact_ground_energy
from vqe import run_vqe


def run_single_experiment(
    n_qubits, a, b, c, depth, seed=64, maxiter=1000
):
    """
    Run one VQE experiment and compare its result
    against exact diagonalization.

    Args:
        n_qubits: Number of qubits
        a, b, c: Hamiltonian coupling coefficients
        depth: Ansatz circuit depth
        seed: Random seed for parameter initialization
        maxiter: Maximum optimizer iterations/evaluations

    Returns:
        Dictionary containing experimental results
    """
    H = build_hamiltonian(n_qubits, a, b, c)
    E_exact = exact_ground_energy(H)
    circuit, theta = build_ansatz(n_qubits, depth)

    rng = np.random.default_rng(seed)
    initial_parameters = rng.uniform(
        0,
        2 * np.pi,
        len(theta)
    )

    result = run_vqe(
        H,
        circuit,
        theta,
        initial_parameters,
        maxiter
    )
    E_vqe = result.fun
    energy_error = abs(E_vqe - E_exact)

    experiment_results = {
        "vqe_energy": E_vqe,
        "exact_energy": E_exact,
        "energy_error": energy_error,
    }
    return experiment_results
