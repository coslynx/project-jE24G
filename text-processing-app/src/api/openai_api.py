import requests

class OpenAIAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1/"

    def improve_text(self, text, options):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": options.get("model", "text-davinci-003"),
            "text": text
        }
        response = requests.post(f"{self.base_url}engines/{data['model']}/completions", headers=headers, json=data)
        
        if response.status_code == 200:
            return response.json()["choices"][0]["text"]
        else:
            return "Error: Failed to improve text. Please try again later."

    def adjust_improvement_level(self, text, options):
        improvement_levels = ["low", "medium", "high"]
        selected_level = options.get("improvement_level", "medium")
        
        if selected_level in improvement_levels:
            options["model"] = f"text-davinci-{improvement_levels.index(selected_level) + 1:03d}"
            return self.improve_text(text, options)
        else:
            return "Error: Invalid improvement level selected."

    def spell_check_text(self, text):
        # Implement spell-checking logic here
        return text

    def process_text(self, text, options):
        improved_text = self.adjust_improvement_level(text, options)
        if "spell_check" in options and options["spell_check"]:
            improved_text = self.spell_check_text(improved_text)
        return improved_text