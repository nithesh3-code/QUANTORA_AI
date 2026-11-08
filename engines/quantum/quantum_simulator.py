from qiskit import transpile
from qiskit_aer import AerSimulator

class LocalQuantumSimulator:
    def __init__(self):
        # Initialize the local CPU-based quantum simulator
        self.simulator = AerSimulator()

    def run_circuit(self, qc, shots=1024):
        """
        Executes a quantum circuit and returns the measurement results.
        'shots' is the number of times we run the circuit to build a probability distribution.
        """
        # 1. Transpile the circuit (optimizes the gates for the simulator backend)
        compiled_circuit = transpile(qc, self.simulator)
        
        # 2. Execute the circuit
        job = self.simulator.run(compiled_circuit, shots=shots)
        
        # 3. Retrieve the measurement counts (how many times we got '00', '01', etc.)
        result = job.result()
        counts = result.get_counts(compiled_circuit)
        
        return counts