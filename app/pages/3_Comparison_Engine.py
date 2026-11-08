import streamlit as st
import sys
import os
import random
from qiskit import QuantumCircuit

# Add the project root directory to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from core.comparison_engine import ComparisonEngine
from engines.quantum.quantum_simulator import LocalQuantumSimulator
from database.db import save_experiment
from app.components.style import apply_custom_css

st.set_page_config(page_title="Comparison Engine", page_icon="⚖️", layout="wide")

# Apply the global quantum theme
apply_custom_css()

st.title("⚖️ Algorithm Comparison Engine")
st.markdown("Benchmark classical algorithms against quantum circuits.")
st.markdown("---")

st.header("Experiment 1: The Fair Coin Flip")
st.markdown("Comparing classical pseudo-random generation against a quantum superposition (Hadamard gate).")

if st.button("Run Comparison Benchmark"):
    with st.spinner("Running benchmarks..."):
        
        # 1. Define the Classical Algorithm
        def run_classical_coin():
            results = {'0': 0, '1': 0}
            for _ in range(1024):
                flip = str(random.randint(0, 1))
                results[flip] += 1
            return results

        # 2. Define the Quantum Algorithm
        def run_quantum_coin():
            qc = QuantumCircuit(1, 1)
            qc.h(0) 
            qc.measure(0, 0)
            simulator = LocalQuantumSimulator()
            return simulator.run_circuit(qc, shots=1024)

        # 3. Execute Comparison
        engine = ComparisonEngine()
        report = engine.benchmark("1024 Coin Flips", run_classical_coin, run_quantum_coin)

        # --- NEW CODE: AUTOMATICALLY SAVE TO DATABASE ---
        save_experiment(
            name="Coin Flip Benchmark", 
            algo_type="Hybrid Comparison", 
            exec_time=report['classical_time_sec'] + report['quantum_time_sec'], 
            result_dict=report
        )
        # ------------------------------------------------

        # 4. Display Results
        st.success("Benchmark Complete & Saved to Database!")
        
        st.subheader("Performance Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Classical Time", f"{report['classical_time_sec']:.5f} s")
        col2.metric("Quantum Time", f"{report['quantum_time_sec']:.5f} s")
        col3.metric("Faster Engine", report['faster_engine'])

        st.subheader("Output Distributions")
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.markdown("**Classical Results**")
            st.bar_chart(report['classical_result'])
        with res_col2:
            st.markdown("**Quantum Results**")
            st.bar_chart(report['quantum_result'])
            
        st.info("💡 **Scientific Note:** The Classical engine will almost always win on execution time here because your laptop is mathematically simulating a quantum computer.")