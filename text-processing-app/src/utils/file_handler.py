import os
import requests
from spellchecker import SpellChecker

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return file.read()
        else:
            raise FileNotFoundError("File not found")

    def write_file(self, content, output_file):
        with open(output_file, 'w') as file:
            file.write(content)

    def spell_check_text(self, text):
        spell = SpellChecker()
        misspelled = spell.unknown(text.split())
        for word in misspelled:
            text = text.replace(word, spell.correction(word))
        return text

    def select_text_range(self, text, start_index, end_index):
        return text[start_index:end_index]

    def process_text(self, text, improvement_level):
        # Code for processing text using OpenAI API based on improvement level
        improved_text = text  # Placeholder for actual processing logic
        return improved_text

    def format_text(self, text, formatting_options):
        # Code for formatting text based on user-defined options
        formatted_text = text  # Placeholder for actual formatting logic
        return formatted_text

    def save_improved_text(self, improved_text, output_file):
        self.write_file(improved_text, output_file)  # Save the improved text to a new file

    def preview_text(self, original_text, improved_text):
        # Display original and improved text side by side for comparison
        preview = f"Original Text:\n{original_text}\n\nImproved Text:\n{improved_text}"
        return preview

    def process_and_save_text(self, improvement_level, formatting_options, output_file):
        text = self.read_file()
        processed_text = self.process_text(text, improvement_level)
        formatted_text = self.format_text(processed_text, formatting_options)
        self.save_improved_text(formatted_text, output_file)