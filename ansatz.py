from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector


def build_ansatz(n_qubits, depth):
    """
    Construct the paramterized quantum circuit. Current 
    implementation is a hardware-efficient ansatz

    Each layer consists of:
        1. Rx and Rz rotations on every qubit.
        2. CNOT gates between neighboring qubits.

    Args:
        n_qubits: Number of qubits
        depth: Number of rotation-entanglement layers

    Returns:
        circuit: Parameterized QuantumCircuit
        theta: ParameterVector of circuit parameters
    """
    circuit = QuantumCircuit(n_qubits)

    num_parameters = 2 * n_qubits * depth
    theta = ParameterVector("theta", num_parameters)
    parameter_index = 0

    for layer in range(depth):
        for qubit in range(n_qubits):
            circuit.ry(theta[parameter_index], qubit)
            parameter_index += 1

            circuit.rz(theta[parameter_index], qubit)
            parameter_index += 1

        for qubit in range(n_qubits - 1):
            circuit.cx(qubit, qubit + 1)

    return circuit, theta
