import random

def moves():
  return ["paper", "rock", "scissors"]

computer_object = ""
user_choice = ""

def get_computer_choice():
  global computer_object
  computer_object = random.choice(moves())

def get_user_choice():
  get_computer_choice()
  global user_choice
  user_choice = input("Choose: ")
  return user_choice

def evaluate(user_choice):
  if computer_object == user_choice:
    print("you both picked the same - go again")
  elif computer_object == "rock" and user_choice == "scissors":
    print("the computer chose rock, you lose")
  elif computer_object == "rock" and user_choice == "paper":
    print("the computer chose rock, you won")
  elif computer_object == "paper" and user_choice == "scissors":
    print("the computer chose paper, you win")
  elif computer_object == "paper" and user_choice == "rock":
    print("the computer chose paper, you lose")
  elif computer_object == "scissors" and user_choice == "paper":
    print("the computer chose scissors, you lose")
  else: 
    print("the computer chose scissors, you win")
