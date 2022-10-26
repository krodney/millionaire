from components.play import play_game

print("Hello! Welcome to 'Who Wants to Be a Millionaire'.")
print("I am your host, Rodney Kimathi. We have a special guest joining us.\n")

name = input("What is your name? ")

print("Welcome to the game {}.\n".format(name))
print("To play, enter the choice A, B, C, or D that represents the correct answer.")
print("The rules are simple, answer questions and win money. Let us begin!")

prize_money = play_game()

print("\nThank you {} for playing 'Who Wants to Be a Millionaire'. Your total prize money is ${}.".format(name, prize_money))
print("See you next time!")
