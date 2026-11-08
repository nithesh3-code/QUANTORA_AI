import sqlite3
import os
import json
from datetime import datetime

# Determine the path for our local database file
DB_PATH = os.path.join(os.path.dirname(__file__), 'quantora_research.db')

def get_connection():
    """Establishes a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)

def init_db():
    """Creates the database tables if they do not exist."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create the experiments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS experiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            experiment_name TEXT NOT NULL,
            algorithm_type TEXT NOT NULL,
            execution_time REAL NOT NULL,
            result_data TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def save_experiment(name, algo_type, exec_time, result_dict):
    """Saves a new experiment record into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # We store the dictionary as a JSON string so it fits in one column
    result_json = json.dumps(result_dict)
    
    cursor.execute('''
        INSERT INTO experiments (timestamp, experiment_name, algorithm_type, execution_time, result_data)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, name, algo_type, exec_time, result_json))
    
    conn.commit()
    conn.close()

def get_all_experiments():
    """Retrieves all saved experiments from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT timestamp, experiment_name, algorithm_type, execution_time, result_data FROM experiments ORDER BY id DESC')
    rows = cursor.fetchall()
    conn.close()
    
    return rows