class Answer:
    def __init__(self, choices):
        self.choices = choices

    def __repr__(self):
        string = ""
        
        for key, value in self.choices.items():
            string += key + ". " + value + "\n"

        return string
