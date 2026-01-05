class ScoreManager:
    def __init__(self):
        self.score = 0
        self.correct_words = 0
        self.wrong_words = 0


    def correct(self):
        self.score += 10
        self.correct_words += 1


    def wrong(self):
        self.wrong_words += 1