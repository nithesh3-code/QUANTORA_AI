import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.classical.classical_knapsack import ClassicalKnapsackSolver
from database.db import save_experiment
from app.components.style import apply_custom_css # <--- IMPORT ADDED

st.set_page_config(page_title="Classical Lab", page_icon="💻", layout="wide")

apply_custom_css() # <--- CSS APPLIED HERE

st.title("💻 Classical Computing Lab")
st.markdown("Run standard optimization algorithms using Google OR-Tools.")
st.markdown("---")

# ... (Leave the rest of the code exactly as it was) ...
st.header("🎒 The Knapsack Problem")
st.markdown("Maximize the total value of items placed in a knapsack without exceeding its weight capacity.")

# UI Input section
col1, col2 = st.columns(2)
with col1:
    values_input = st.text_input("Item Values (comma-separated)", "50, 60, 140, 10, 80")
    weights_input = st.text_input("Item Weights (comma-separated)", "10, 20, 30, 5, 15")
with col2:
    capacity_input = st.number_input("Knapsack Weight Capacity", min_value=1, value=50, step=1)

# Execution Button
if st.button("Solve Classical Knapsack"):
    try:
        # 1. Parse the text inputs
        values = [int(v.strip()) for v in values_input.split(",")]
        weights = [[int(w.strip()) for w in weights_input.split(",")]] 
        capacities = [int(capacity_input)] 

        # 2. Validate input lengths
        if len(values) != len(weights[0]):
            st.error("Error: The number of values must match the number of weights.")
        else:
            # 3. Run the solver
            solver = ClassicalKnapsackSolver()
            result = solver.solve(values, weights, capacities)

            # --- NEW CODE: AUTOMATICALLY SAVE TO DATABASE ---
            save_experiment(
                name="Knapsack Optimization", 
                algo_type="Classical (OR-Tools)", 
                exec_time=result["execution_time_seconds"], 
                result_dict=result
            )
            # ------------------------------------------------

            # 4. Display Results
            st.success("Optimization Complete & Saved to Database!")
            st.subheader("Results")
            
            res_col1, res_col2, res_col3 = st.columns(3)
            res_col1.metric("Maximum Value Found", result["total_value"])
            res_col2.metric("Total Weight Used", f'{result["total_weight"]} / {capacity_input}')
            res_col3.metric("Execution Time", f"{result['execution_time_seconds']:.6f} s")

            st.info(f"**Packed Item Indices:** {result['packed_items']}")
            
    except ValueError:
        st.error("Please ensure all inputs are valid numbers separated by commas.")