import tkinter as tk
import requests
from utils.file_handler import save_text_to_file
from utils.text_formatter import format_text
from spell_checker import spell_check_text
from api.openai_api import improve_text
from user_interface import display_text_comparison

class TextProcessorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Processor App")
        
        self.original_text = ""
        self.improved_text = ""
        
        self.create_widgets()
        
    def create_widgets(self):
        self.text_input = tk.Text(self.root, height=10, width=50)
        self.text_input.pack()
        
        self.process_button = tk.Button(self.root, text="Process Text", command=self.process_text)
        self.process_button.pack()
        
        self.save_button = tk.Button(self.root, text="Save Improved Text", command=self.save_improved_text)
        self.save_button.pack()
        
    def process_text(self):
        self.original_text = self.text_input.get("1.0", "end-1c")
        
        if not self.original_text:
            tk.messagebox.showerror("Error", "Please enter some text to process.")
            return
        
        improved_text = improve_text(self.original_text)
        self.improved_text = spell_check_text(improved_text)
        
        display_text_comparison(self.original_text, self.improved_text)
        
    def save_improved_text(self):
        if not self.improved_text:
            tk.messagebox.showerror("Error", "No improved text to save.")
            return
        
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        save_text_to_file(file_path, self.improved_text)
        
if __name__ == "__main__":
    app = TextProcessorApp()
    app.root.mainloop()