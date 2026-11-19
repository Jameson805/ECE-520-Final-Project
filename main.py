import argparse

from experiments import run_single_experiment


def main():
    parser = argparse.ArgumentParser(
        description="Heisenberg VQE Simulation"
    )
    parser.add_argument("--n-qubits", type=int, default=2)
    parser.add_argument("--a", type=float, default=1.0)
    parser.add_argument("--b", type=float, default=1.0)
    parser.add_argument("--c", type=float, default=1.0)
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--seed", type=int, default=64)
    parser.add_argument("--maxiter", type=int, default=1000)
    args = parser.parse_args()

    results = run_single_experiment(
        n_qubits=args.n_qubits,
        a=args.a,
        b=args.b,
        c=args.c,
        depth=args.depth,
        seed=args.seed,
        maxiter=args.maxiter
    )

    print("\n--- VQE Experiment Results ---")
    print(f"Number of qubits: {args.n_qubits}")
    print(f"Hamiltonian coefficients: a={args.a}, b={args.b}, c={args.c}")
    print(f"Ansatz depth: {args.depth}")
    print(f"VQE energy: {results['vqe_energy']:.8f}")
    print(f"Exact energy: {results['exact_energy']:.8f}")
    print(f"Energy error: {results['energy_error']:.8e}")


if __name__ == "__main__":
    main()
