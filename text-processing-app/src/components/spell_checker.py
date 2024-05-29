import pyttsx3
from spellchecker import SpellChecker

class SpellChecker:
    def __init__(self):
        self.spell = SpellChecker()

    def check_spelling(self, text):
        words = text.split()
        misspelled = self.spell.unknown(words)
        return misspelled

    def correct_spelling(self, text):
        words = text.split()
        corrected_text = []
        for word in words:
            corrected_text.append(self.spell.correction(word))
        return " ".join(corrected_text)