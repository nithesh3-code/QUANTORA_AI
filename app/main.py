import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from app.components.style import apply_custom_css

st.set_page_config(page_title="QUANTORA AI", page_icon="⚛️", layout="wide", initial_sidebar_state="expanded")

# Apply our global CSS
apply_custom_css()

st.title("⚛️ QUANTORA AI")
st.subheader("Explore Problems. Compare Intelligence. Discover Quantum Possibilities.")
st.markdown("---")
st.markdown("""
Welcome to the QUANTORA AI Research Platform. 
This is a local-first hybrid quantum-classical AI environment designed for experimentation and learning.

### 🚀 Available Modules:
Use the sidebar on the left to navigate through the laboratories.
""")
st.sidebar.title("Navigation Menu")
st.sidebar.info("Select a lab from the pages above to begin your research.")