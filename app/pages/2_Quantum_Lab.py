import streamlit as st
import sys
import os
import json
import time

# Ensure Python can find the algorithms module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.quantum.bell_state import run_bell_state
from algorithms.quantum.grover import run_grover_search
from database.db import save_experiment
from app.components.style import apply_custom_css

st.set_page_config(page_title="Quantum Lab", page_icon="⚛️", layout="wide")
apply_custom_css()

st.title("⚛️ Quantum Lab")
st.markdown("Simulate quantum circuits using Qiskit Aer on your local hardware.")
st.markdown("---")

algorithm_choice = st.radio("Select Quantum Algorithm:", ["Bell State (Entanglement)", "Grover's Search (Database Search)"])

shots = st.slider("Measurement Shots:", min_value=100, max_value=4000, value=1024, step=100)

if st.button("Run Quantum Simulation"):
    with st.spinner("Initializing Quantum Simulator..."):
        start_time = time.perf_counter()
        
        if algorithm_choice == "Bell State (Entanglement)":
            results = run_bell_state(shots=shots)
            exp_name = "Bell State Simulation"
        else:
            results = run_grover_search(shots=shots)
            exp_name = "Grover's Quantum Search"
            
        execution_time = time.perf_counter() - start_time
        
        # Save to SQLite (using the exact keywords from Classical Lab)
        save_experiment(
            name=exp_name,
            algo_type="Quantum (Qiskit Aer)",
            exec_time=execution_time, 
            result_dict=json.dumps(results)
        )
        
        st.success(f"Simulation Complete in {execution_time:.4f} seconds!")
        
        st.subheader("Measurement Counts")
        st.bar_chart(results["counts"])
        
        st.markdown("**Raw Output:**")
        st.code(json.dumps(results, indent=2), language="json")