import random
options = ["paper", "rock", "scissors"]
# Prompt computer to make a choice
def get_computer_choice():
  global computer_object
  # Randomly select an object for the computer's choice
  computer_object = random.choice(options)

# defining global variable https://www.w3schools.com/PYTHON/python_scope.asp
computer_object = ""
user_choice = ""
# make computer select a new option when user does
def get_user_choice():
  get_computer_choice()
  global user_choice
  user_choice = input("Choose: ")
# handle user playing again: if y, prompt for another choice, if n end game, if neither ask again
def restart():
  user_input = input("would you like to play again? ")
  if not user_input in ["y", "n"]:
    print("please select using y or n")
    restart()
  elif user_input == "y":
    play()
  else:
    print("thanks for playing")
# determine who wins, user or computer
def evaluate(user_choice):
  if computer_object == user_choice:
    print("you both picked the same - go again")
    play()
  elif computer_object == "rock" and user_choice == "scissors":
    print(computer_object, user_choice)
    print("the computer chose rock, you lose")
  elif computer_object == "rock" and user_choice == "paper":
    print(computer_object, user_choice)
    print("the computer chose rock, you won")
  elif computer_object == "paper" and user_choice == "scissors":
    print(computer_object, user_choice)
    print("the computer chose paper, you win")
  elif computer_object == "paper" and user_choice == "rock":
    print(computer_object, user_choice)
    print("the computer chose paper, you lose")
  elif computer_object == "scissors" and user_choice == "paper":
    print(computer_object, user_choice)
    print("the computer chose scissors, you lose")
  else: 
    print(computer_object, user_choice)
    print("the computer chose scissors, you win")
# check user choice is one of paper, rock, scissors, and evaluate if valid option
def play():
  get_user_choice()
  if not user_choice in options:
    print("You must choose paper, rock or scissors")
    restart()
  else:
    evaluate(user_choice)

play()