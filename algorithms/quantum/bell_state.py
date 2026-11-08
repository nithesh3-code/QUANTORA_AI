from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def run_bell_state(shots=1024):
    """Creates a 2-qubit Bell State (maximum entanglement)."""
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=shots).result()
    
    return {
        "algorithm": "Quantum (Qiskit Aer)",
        "shots": shots,
        "counts": result.get_counts(qc)
    }