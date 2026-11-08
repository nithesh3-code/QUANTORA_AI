import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
        .stApp { background-color: #050510; color: #e0e0e0; }
        
        h1, h2, h3 {
            color: #00FFFF !important;
            text-shadow: 0px 0px 15px rgba(0, 255, 255, 0.4);
            font-family: 'Courier New', Courier, monospace;
        }

        /* Buttons */
        div.stButton > button {
            background: linear-gradient(90deg, #0f0c29, #302b63, #24243e);
            color: #00FFFF; border: 1px solid #00FFFF;
            box-shadow: 0px 0px 10px rgba(0, 255, 255, 0.3);
            border-radius: 5px; transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            border-color: #FF00FF; color: #FFFFFF;
            box-shadow: 0px 0px 20px rgba(255, 0, 255, 0.6);
            transform: scale(1.02);
        }

        /* Buttons (Standard & Download) */
        div.stButton > button, 
        [data-testid="stDownloadButton"] > button {
            background: linear-gradient(90deg, #0f0c29, #302b63, #24243e) !important;
            color: #00FFFF !important; 
            border: 1px solid #00FFFF !important;
            box-shadow: 0px 0px 10px rgba(0, 255, 255, 0.3) !important;
            border-radius: 5px !important; 
            transition: all 0.3s ease !important;
        }
        div.stButton > button:hover, 
        [data-testid="stDownloadButton"] > button:hover {
            border-color: #FF00FF !important; 
            color: #FFFFFF !important;
            box-shadow: 0px 0px 20px rgba(255, 0, 255, 0.6) !important;
            transform: scale(1.02) !important;
        }

        /* Text & Number Inputs */
        .stTextInput > div > div > input, .stNumberInput > div > div > input {
            background-color: #050510 !important;
            color: #00FFFF !important;
        }
        div[data-baseweb="input"] {
            background-color: #050510 !important;
            border: 1px solid #302b63 !important;
            border-radius: 5px;
            transition: all 0.3s ease-in-out;
        }
        div[data-baseweb="input"]:focus-within, div[data-baseweb="input"]:hover {
            border-color: #00FFFF !important;
            box-shadow: 0px 0px 15px rgba(0, 255, 255, 0.5) !important;
        }

        /* --- NEW: Dropdown Menus (Selectboxes) --- */
        div[data-baseweb="select"] > div {
            background-color: #050510 !important;
            border: 1px solid #302b63 !important;
            color: #00FFFF !important;
        }
        div[data-baseweb="select"] > div:hover {
            border-color: #00FFFF !important;
            box-shadow: 0px 0px 15px rgba(0, 255, 255, 0.5) !important;
        }
        /* Dropdown menu list items */
        ul[data-baseweb="menu"] {
            background-color: #0a0a1a !important;
            border: 1px solid #00FFFF !important;
        }
        li[data-baseweb="menu-item"] {
            color: #00FFFF !important;
        }
        li[data-baseweb="menu-item"]:hover {
            background-color: #302b63 !important;
            color: #FFFFFF !important;
        }

        /* --- NEW: Code Blocks (st.code) --- */
        pre {
            background-color: #0a0a1a !important;
            border: 1px solid #FF00FF !important;
            box-shadow: 0px 0px 10px rgba(255, 0, 255, 0.2);
            border-radius: 5px;
        }
        code {
            color: #00FFFF !important;
            font-family: 'Courier New', Courier, monospace !important;
        }

        /* Sliders and Metrics */
        div[data-baseweb="slider"] { filter: drop-shadow(0px 0px 5px rgba(0, 255, 255, 0.5)); }
        [data-testid="stMetricValue"] {
            color: #00FFFF !important;
            text-shadow: 0px 0px 15px rgba(0, 255, 255, 0.6);
            font-family: 'Courier New', Courier, monospace;
        }
        [data-testid="stMetricLabel"] {
            color: #FF00FF !important;
            font-weight: bold;
        }
        
        [data-testid="stSidebar"] {
            background-color: #020208;
            border-right: 1px solid #302b63;
        }

        /* HTML Tables */
        table {
            border-collapse: collapse !important;
            width: 100% !important;
            background-color: #050510 !important;
            color: #00FFFF !important;
            border: 1px solid #00FFFF !important;
            box-shadow: 0px 0px 15px rgba(0, 255, 255, 0.3) !important;
        }
        th {
            border: 1px solid #FF00FF !important;
            background-color: #0a0a1a !important;
            color: #FF00FF !important;
            text-align: center !important;
            font-family: 'Courier New', Courier, monospace;
            text-shadow: 0px 0px 10px rgba(255, 0, 255, 0.5);
        }
        td {
            border: 1px solid #302b63 !important;
            text-align: center !important;
        }
        tbody tr:hover { background-color: #100b2e !important; }
        th:first-child, td:first-child { display: none; }
    </style>
    """, unsafe_allow_html=True)