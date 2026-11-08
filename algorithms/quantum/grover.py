from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def run_grover_search(shots=1024):
    """
    Runs a 2-qubit Grover search specifically tuned to find the state |11>.
    """
    qc = QuantumCircuit(2, 2)
    
    # 1. Initialization
    qc.h([0, 1])
    qc.barrier()
    
    # 2. Oracle
    qc.cz(0, 1)
    qc.barrier()
    
    # 3. Diffuser
    qc.h([0, 1])
    qc.z([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])
    qc.barrier()
    
    # 4. Measurement
    qc.measure([0, 1], [0, 1])
    
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=shots).result()
    counts = result.get_counts(qc)
    
    return {
        "algorithm": "Grover Search",
        "target_state": "11",
        "shots": shots,
        "counts": counts
    }