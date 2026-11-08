import time

class ComparisonEngine:
    def __init__(self):
        """Initializes the engine to compare Classical vs Quantum performance."""
        pass

    def benchmark(self, experiment_name, classical_runner, quantum_runner):
        """
        Takes two functions (one classical, one quantum), executes them,
        and records their execution time and results.
        """
        # 1. Benchmark Classical Algorithm
        start_c = time.perf_counter()
        classical_result = classical_runner()
        time_c = time.perf_counter() - start_c

        # 2. Benchmark Quantum Algorithm
        start_q = time.perf_counter()
        quantum_result = quantum_runner()
        time_q = time.perf_counter() - start_q

        # 3. Compile Comparison Report
        return {
            "experiment": experiment_name,
            "classical_time_sec": time_c,
            "quantum_time_sec": time_q,
            "classical_result": classical_result,
            "quantum_result": quantum_result,
            "speed_difference": abs(time_c - time_q),
            "faster_engine": "Classical" if time_c < time_q else "Quantum"
        }