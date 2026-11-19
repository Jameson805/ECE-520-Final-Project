from qiskit.quantum_info import SparsePauliOp


def build_hamiltonian(n_qubits, a, b, c):
    """
    Build the hamiltonian given entry parameters
    H = sum_i (a XX + b YY + c ZZ)

    Args:
        n_qubits: Number of qubits in the chain
        a: XX interaction coefficient
        b: YY interaction coefficient
        c: ZZ interaction coefficient

    Returns:
        SparsePauliOp: Hamiltonian operator
    """
    terms = []

    for i in range(n_qubits - 1):
        terms.append(("XX", [i, i + 1], a))
        terms.append(("YY", [i, i + 1], b))
        terms.append(("ZZ", [i, i + 1], c))

    hamiltonian = SparsePauliOp.from_sparse_list(
        terms,
        num_qubits=n_qubits
    )
    return hamiltonian
