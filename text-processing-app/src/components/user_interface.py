import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from text_processor import process_text
from spell_checker import spell_check_text
from file_handler import save_text_to_file
from openai_api import improve_text

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Processing Application")

        self.original_text = tk.Text(self.root, height=10, width=50)
        self.original_text.pack()

        self.edit_text_button = tk.Button(self.root, text="Edit Text", command=self.edit_text)
        self.edit_text_button.pack()

        self.save_text_button = tk.Button(self.root, text="Save Text", command=self.save_text)
        self.save_text_button.pack()

        self.preview_text_button = tk.Button(self.root, text="Preview Text", command=self.preview_text)
        self.preview_text_button.pack()

        self.progress_bar = tk.Label(self.root, text="Progress: 0%")
        self.progress_bar.pack()

        self.root.mainloop()

    def edit_text(self):
        text_to_improve = self.original_text.get("1.0", tk.END)
        try:
            improved_text = improve_text(text_to_improve)
            self.original_text.delete("1.0", tk.END)
            self.original_text.insert(tk.END, improved_text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def save_text(self):
        text_to_save = self.original_text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                save_text_to_file(text_to_save, file_path)
                messagebox.showinfo("Success", "Text saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def preview_text(self):
        text_to_preview = self.original_text.get("1.0", tk.END)
        try:
            improved_text = improve_text(text_to_preview)
            messagebox.showinfo("Preview", f"Improved Text:\n{improved_text}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    UserInterface()