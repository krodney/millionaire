from components.answer import Answer
from components.question import Question

questions = {
    1: ["What sort of animal is Walt Disney's Dumbo?", "C"],
    2: ["What was the name of the Spanish waiter in the TV sitcom 'Fawlty Towers'?", "A"],
    3: ["Which battles took place between the Royal Houses of York and Lancaster?", "C"],
    4: ["Which former Beatle narrated the TV adventures of Thomas the Tank Engine?", "D"],
    5: ["Queen Anne was the daughter of which English Monarch?", "A"],
    6: ["Who composed 'Rhapsody in Blue'?", "B"],
    7: ["What is the Celsius equivalent of 77 degrees Fahrenheit?", "C"],
    8: ["Suffolk Punch and Hackney are types of what?", "D"],
    9: ["Which Shakespeare play features the line 'Neither a borrower nor a lender be'?", "A"],
    10: ["Which is the largest city in the USA's largest state?", "D"],
    11: ["The word 'aristocracy' literally means power in the hands of whom?", "B"],
    12: ["Where would a 'peruke' be worn?", "B"],
    13: ["In which palace was Queen Elizabeth I born?", "A"],
    14: ["From which author's work did scientists take the word 'quark'?", "C"],
    15: ["Which of these islands was ruled by Britain from 1815 until 1864?", "D"]
}

answers = {
    1: {"A": "Deer", "B": "Rabbit", "C": "Elephant", "D": "Donkey"},
    2: {"A": "Manuel", "B": "Pedro", "C": "Alfonso", "D": "Javier"},
    3: {"A": "Thirty Years War", "B": "Hundred Years War", "C": "War of the Roses", "D": "English Civil War"},
    4: {"A": "John Lennon", "B": "Paul McCartney", "C": "George Harrison", "D": "Ringo Starr"},
    5: {"A": "James II", "B": "Henry VIII", "C": "Victoria", "D": "William I"},
    6: {"A": "Irving Berlin", "B": "George Gershwin", "C": "Aaron Copland", "D": "Cole Porter"},
    7: {"A": "15", "B": "20", "C": "25", "D": "30"},
    8: {"A": "Carriage", "B": "Wrestling style", "C": "Cocktail", "D": "Horse"},
    9: {"A": "Hamlet", "B": "Macbeth", "C": "Othello", "D": "The Merchant of Venice"},
    10: {"A": "Dallas", "B": "Los Angeles", "C": "New York", "D": "Anchorage"},
    11: {"A": "The few", "B": "The best", "C": "The barons", "D": "The rich"},
    12: {"A": "Around the neck", "B": "On the head", "C": "Around the waist", "D": "On the wrist"},
    13: {"A": "Greenwich", "B": "Richmond", "C": "Hampton Court", "D": "Kensington"},
    14: {"A": "Lewis Carroll", "B": "Edward Lear", "C": "James Joyce", "D": "Aldous Huxley"},
    15: {"A": "Crete", "B": "Cyprus", "C": "Corsica", "D": "Corfu"},
}

def setup_game():
    game = {}

    for i in range(1, len(questions)+1):
        game[i] = Question(questions[i][0], Answer(answers[i]), questions[i][1])

    return game
