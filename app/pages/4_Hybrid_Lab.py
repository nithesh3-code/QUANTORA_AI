import streamlit as st
import sys
import os

# Add the project root directory to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.hybrid.hybrid_optimizer import HybridQuantumOptimizer
from database.db import save_experiment
from app.components.style import apply_custom_css

st.set_page_config(page_title="Hybrid Lab", page_icon="🔗", layout="wide")

# Apply the global quantum theme
apply_custom_css()

st.title("🔗 Hybrid Quantum-Classical Lab")
st.markdown("Watch a classical optimizer (SciPy) train a quantum circuit (Qiskit) to maximize a specific state.")
st.markdown("---")

st.header("Variational Quantum Optimization")
st.markdown("**Our Goal:** Train the quantum circuit to output the '11' state as often as possible by letting SciPy automatically tweak two rotation angles.")

if st.button("Start Hybrid Optimization"):
    with st.spinner("Classical and Quantum engines are looping... please wait!"):
        
        # 1. Run our hybrid engine
        optimizer = HybridQuantumOptimizer()
        result = optimizer.optimize()

        # --- NEW CODE: AUTOMATICALLY SAVE TO DATABASE ---
        # We convert the numpy array of angles to a standard list so it can be saved as JSON
        save_result = result.copy()
        save_result["optimal_angles"] = list(save_result["optimal_angles"])
        
        save_experiment(
            name="VQE Parameter Optimization", 
            algo_type="Hybrid (SciPy + Qiskit)", 
            exec_time=result['time_seconds'], 
            result_dict=save_result
        )
        # ------------------------------------------------

        # 2. Display Metrics
        st.success(f"Optimization Complete in {result['iterations']} iterations & Saved to Database!")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Max Probability of '11'", f"{result['max_probability']:.2%}")
        col2.metric("Optimal Angle 1", f"{result['optimal_angles'][0]:.4f} rad")
        col3.metric("Optimal Angle 2", f"{result['optimal_angles'][1]:.4f} rad")
        
        # 3. Display the Learning Curve
        st.subheader("Training Progress (Learning Curve)")
        st.markdown("This chart shows how the classical optimizer improved the quantum circuit's probability of hitting '11' over time.")
        
        st.line_chart(result['history'])
        
        st.info(f"**Execution Time:** {result['time_seconds']:.4f} seconds")