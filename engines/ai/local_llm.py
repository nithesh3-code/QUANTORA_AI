import time
import requests

class GroqAIAssistant:
    def __init__(self):
        # ⚠️ Paste your active Groq API Key here! (starts with gsk_...)
        self.api_key = "YOUR_GROQ_API_KEY"
        self.endpoint = "https://api.groq.com/openai/v1/chat/completions"

    def analyze_results(self, experiment_name, result_data):
        prompt = f"Briefly explain the scientific significance of this experiment: {experiment_name}. The results were: {result_data}."
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "openai/gpt-oss-120b", 
            "messages": [
                {
                    "role": "system", 
                    "content": "You are an elite quantum computing and classical algorithm research assistant. Keep your analysis brief, highly scientific, and directly related to the provided data. IMPORTANT: You must format all mathematical equations and LaTeX using standard Markdown. Use single $ for inline math and double $$ for block equations. Do NOT use \\[ or \\]."
                },
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
        
        start_time = time.perf_counter()
        
        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status() 
            insight = response.json()['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            try:
                error_details = response.json()
            except:
                error_details = response.text if 'response' in locals() and response else "No response body"
            insight = f"API Connection Error: {e}\n\n**Details:** {error_details}"
            
        execution_time = time.perf_counter() - start_time
        
        return {
            "prompt": prompt,
            "insight": insight,
            "inference_time_sec": execution_time
        }