from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from scipy.optimize import minimize
import time

class HybridQuantumOptimizer:
    def __init__(self):
        self.simulator = AerSimulator()
        self.iteration_history = []

    def create_parameterized_circuit(self, theta):
        """
        Creates a 2-qubit quantum circuit where the gates are controlled 
        by classical parameters (theta).
        """
        qc = QuantumCircuit(2)
        qc.h([0, 1])             # Initial superposition
        qc.rx(theta[0], 0)       # Rotate Qubit 0 by angle theta[0]
        qc.rx(theta[1], 1)       # Rotate Qubit 1 by angle theta[1]
        qc.cx(0, 1)              # Entangle them
        qc.measure_all()
        return qc

    def objective_function(self, theta):
        """
        This is the bridge between Classical and Quantum. 
        SciPy calls this function to test its current guess for 'theta'.
        """
        # 1. Build and run the circuit with the current classical guess
        qc = self.create_parameterized_circuit(theta)
        compiled = transpile(qc, self.simulator)
        result = self.simulator.run(compiled, shots=512).result()
        counts = result.get_counts()
        
        # 2. Our goal is to maximize the probability of getting the '11' state.
        # SciPy only knows how to *minimize*, so we return negative probability.
        prob_11 = counts.get('11', 0) / 512.0
        cost = -prob_11 
        
        # Save history for our UI visualization
        self.iteration_history.append(prob_11)
        
        return cost

    def optimize(self):
        """Runs the classical-quantum loop."""
        self.iteration_history = [] # Reset history
        initial_guess = [0.0, 0.0]  # Start with zero rotation
        
        start_time = time.perf_counter()
        
        # SciPy's COBYLA optimizer takes control here
        result = minimize(self.objective_function, initial_guess, method='COBYLA', options={'maxiter': 50})
        
        execution_time = time.perf_counter() - start_time
        
        return {
            "optimal_angles": result.x,
            "max_probability": -result.fun, # Convert back to positive
            "iterations": result.nfev,
            "history": self.iteration_history,
            "time_seconds": execution_time
        }