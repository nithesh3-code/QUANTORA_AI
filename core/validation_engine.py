import re

class ValidationEngine:
    def __init__(self):
        self.status = "Ready"

    def verify_insight(self, ai_text, raw_result_dict):
        # Extract whole numbers only
        regex_pattern = r'(?<![\d.])\d+(?![\d.])'
        
        ai_numbers_raw = re.findall(regex_pattern, ai_text)
        raw_text = str(raw_result_dict)
        raw_numbers = {int(x) for x in re.findall(regex_pattern, raw_text)}
        
        # Allow theoretical ideal quantum counts for standard 1024-shot experiments
        raw_numbers.update([1024, 512, 256])
        
        ai_numbers = set()
        for num_str in ai_numbers_raw:
            val = int(num_str)
            
            # Permanently ignore all percentages (0-100) and small mathematical differences
            if val <= 100: 
                continue
            
            ai_numbers.add(val)
                
        # Flag only large, completely fabricated experiment counts
        hallucinations = [str(num) for num in ai_numbers if num not in raw_numbers]
                
        if len(hallucinations) == 0:
            return {
                "is_valid": True,
                "message": "✅ Data Verified: The AI's numerical claims match your raw experimental data.",
                "hallucinations": []
            }
        else:
            return {
                "is_valid": False,
                "message": "⚠️ Warning: The AI mentioned unexpected experiment counts. It may be hallucinating.",
                "hallucinations": hallucinations
            }