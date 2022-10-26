class Question:
    def __init__(self, title, answers, correct_answer):
        self.title = title
        self.answers = answers
        self.correct_answer = correct_answer

    def __repr__(self):
        return self.title + "\n" + str(self.answers)
