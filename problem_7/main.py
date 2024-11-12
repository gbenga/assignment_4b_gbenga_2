from .game import moves, get_user_choice, evaluate
options = moves()

def play():
  user_choice = get_user_choice()
  if not user_choice in options:
    print("You must choose paper, rock or scissors")
  else:
    evaluate(user_choice)
  restart()

def restart():
  user_input = input("would you like to play again? ")
  if not user_input in ["y", "n"]:
    print("please select using y or n")
    restart()
  elif user_input == "y":
    play()
  else:
    print("thanks for playing")

def main():
  play()
    
if __name__ == "__main__":
  main()