import numpy as np
from qiskit.quantum_info import Statevector
from scipy.optimize import minimize


def calculate_energy(circuit, theta, parameter_values, hamiltonian):
    """
    Calculate <psi(theta)|H|psi(theta)> for a given
    set of circuit parameters.

    Args:
        circuit: Parameterized quantum circuit
        theta: ParameterVector used in the circuit
        parameter_values: Numerical values for circuit parameters
        hamiltonian: Hamiltonian operator

    Returns:
        float: Expected energy
    """
    parameter_map = dict(zip(theta, parameter_values))
    bound_circuit = circuit.assign_parameters(parameter_map)
    state = Statevector.from_instruction(bound_circuit)
    energy = state.expectation_value(hamiltonian)
    return float(np.real(energy))


def run_vqe(hamiltonian, circuit, theta, initial_parameters, maxiter=1000):
    """
    Minimize the expected energy using a classical optimizer.

    Args:
        hamiltonian: Hamiltonian operator
        circuit: Parameterized quantum circuit
        theta: ParameterVector used in the circuit
        initial_parameters: Initial numerical parameter values
        maxiter: Maximum number of optimizer iterations/evaluations

    Returns:
        OptimizeResult: Result from scipy.optimize.minimize
    """
    initial_parameters = np.asarray(initial_parameters, dtype=float)
    if initial_parameters.shape != (len(theta),):
        raise ValueError("Incorrect number of initial parameters")

    # Objective function to minimize
    def objective(parameter_values):
        return calculate_energy(
            circuit,
            theta,
            parameter_values,
            hamiltonian
        )

    # Classical optimization using COBYLA
    result = minimize(
        objective,
        initial_parameters,
        method="COBYLA",
        options={"maxiter": maxiter}
    )
    return result
