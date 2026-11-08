import streamlit as st
import pandas as pd
import sys
import os

# Add project root path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from database.db import get_all_experiments
from app.components.style import apply_custom_css

st.set_page_config(page_title="Research Dashboard", page_icon="📊", layout="wide")
apply_custom_css()

st.title("📊 Research Dashboard")
st.markdown("View and export your historical quantum and classical experiment data.")
st.markdown("---")

# Fetch all records from SQLite
experiments = get_all_experiments()

if not experiments:
    st.info("No experiments found. Run a simulation in the Classical or Quantum Lab first!")
else:
    # Convert database results into a Pandas DataFrame for easy viewing
    df = pd.DataFrame(experiments, columns=["ID", "Experiment Name", "Algorithm Type", "Timestamp", "Results"])
    
    # Display as an interactive table
    # Display as a raw HTML table to inherit the glowing custom CSS
    st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # --- NEW: CSV Export Feature ---
    st.subheader("💾 Export Data")
    
    # Convert DataFrame to CSV string
    csv_data = df.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="Download Results as CSV",
        data=csv_data,
        file_name="quantora_experiments.csv",
        mime="text/csv",
    )