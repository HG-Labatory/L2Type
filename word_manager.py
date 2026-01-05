import random


class WordManager:
    def __init__(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            self.words = [line.strip() for line in f if line.strip()]


    def get_word(self):
        return random.choice(self.words)