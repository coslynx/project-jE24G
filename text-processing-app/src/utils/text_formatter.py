class TextFormatter:
    def __init__(self, original_text):
        self.original_text = original_text
        self.improved_text = ""

    def improve_text(self, api_response):
        self.improved_text = api_response

    def save_improved_text(self, file_path):
        try:
            with open(file_path, 'w') as file:
                file.write(self.improved_text)
                return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False

    def display_comparison(self):
        print("Original Text:")
        print(self.original_text)
        print("Improved Text:")
        print(self.improved_text)

    def spell_check_text(self, spell_checker):
        self.original_text = spell_checker.correction(self.original_text)
        self.improved_text = spell_checker.correction(self.improved_text)

    def select_text_portion(self, start, end):
        self.original_text = self.original_text[start:end]
        self.improved_text = self.improved_text[start:end]