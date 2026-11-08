import streamlit as st
import sys
import os

# Add project root path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from database.db import get_all_experiments
from app.components.style import apply_custom_css

# Page config MUST be the first Streamlit command
st.set_page_config(page_title="AI Assistant", page_icon="🧠", layout="wide")
apply_custom_css()

st.title("🧠 Local AI Research Assistant")
st.markdown("Analyze your past quantum and classical experiments using an offline, on-device AI model.")
st.markdown("---")

# Fetch historical experiments
experiments = get_all_experiments()

if not experiments:
    st.warning("No experiments found in the database. Run some labs first!")
else:
    st.header("Select Data for Analysis")
    
    # Create a formatted list for the dropdown menu
    experiment_options = {f"{row[1]} ({row[0]})": row for row in experiments}
    selected_name = st.selectbox("Choose an experiment to analyze:", list(experiment_options.keys()))
    
    selected_row = experiment_options[selected_name]
    exp_name = selected_row[1]
    algo_type = selected_row[2]
    result_data = selected_row[4]
    
    # Display the selected raw data
    st.markdown("**Raw Database Record:**")
    st.code(f"Algorithm: {algo_type}\nResults: {result_data}", language="json")
    
    st.markdown("---")
    
    if st.button("Generate AI Insight"):
        st.info("💡 **Note:** Connecting to Groq AI...")
        
        with st.spinner("Analyzing data via Groq (GPT-OSS 120B)..."):
            
            # --- LAZY IMPORTS --- 
            from engines.ai.local_llm import GroqAIAssistant
            from core.validation_engine import ValidationEngine
            
            # 1. Run AI Analysis
            assistant = GroqAIAssistant()
            analysis = assistant.analyze_results(exp_name, result_data)
            
            # 2. Run Mathematical Validation
            validator = ValidationEngine()
            validation_report = validator.verify_insight(analysis["insight"], result_data)
            
            st.success("AI Analysis Complete!")
            
            # 3. Display Validation UI Shield
            if validation_report["is_valid"]:
                st.success(validation_report["message"])
            else:
                st.warning(validation_report["message"])
                st.error(f"**Unverified Numbers Detected:** {', '.join(validation_report['hallucinations'])}")
            
            # --- NEW: Clean up the AI's LaTeX math formatting ---
            clean_insight = analysis["insight"].replace("\\[", "$$").replace("\\]", "$$").replace("[ \\", "$$ \\").replace(" ]", " $$")
            
            st.subheader("Scientific Insight")
            st.write(clean_insight)
            
            st.caption(f"Inference Time: {analysis['inference_time_sec']:.4f} seconds | Model: Groq openai/gpt-oss-120b")