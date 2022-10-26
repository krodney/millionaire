import random
from components.prize import Prize
from components.setup import setup_game

def play_game():
    game = setup_game()
    correct_answers = 0
    number_of_questions = len(game)

    for i in range(1, number_of_questions+1):
        question_number = random.choice(list(game.keys()))
        question = game[question_number]
        
        set_question(i, number_of_questions, question)
        if get_answer() != question.correct_answer:
            print("\nI am afraid that is the wrong answer. The correct answer is {}.".format(question.correct_answer))
            break

        game.pop(question_number)
        correct_answers += 1
        
        print("\nThat is the correct answer!")
        print("Your current prize money is ${}.".format(Prize.amounts[correct_answers]))

    return calculate_prize(correct_answers)

def set_question(current_iteration, number_of_questions, question):
    question_string = "\nFor ${prize}, this is question {question} out of a possible {total}:\n{question}. {title}".format(
        prize=Prize.amounts[current_iteration],
        question=current_iteration,
        total=number_of_questions,
        title=question.title
    )

    print(question_string)
    print(question.answers)

def get_answer():
    answer = input("Answer: ")

    if answer.upper() not in ["A", "B", "C", "D"]:
        print("Invalid answer! Try again.")
        get_answer()

    return answer.upper()

def calculate_prize(correct_answers):
    if correct_answers < Prize.first_checkpoint:
        return Prize.amounts[0]

    if correct_answers < Prize.second_checkpoint:
        return Prize.amounts[Prize.first_checkpoint]
    
    if correct_answers < Prize.third_checkpoint:
        return Prize.amounts[Prize.second_checkpoint]

    return Prize.amounts[-1]
