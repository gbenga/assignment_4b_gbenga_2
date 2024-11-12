import random

guesses_remaining = 5
letter = ""
part_word = ""
random_word = ""

def greeting():
  print("Let's Play Hangman ¯\\_(ツ)_/¯")

def create_part_word():
  global part_word
  temp = []
  for r in random_word:
    temp.append("_")
  part_word = "".join(temp)

def choose_word():
  f_handle = open(f'./problem_8/common_words.txt','r').read()
  words = f_handle.strip().split("\n")
  random_index = random.randint(0, len(words) - 1)
  return words[random_index]

random_word = choose_word()
print(random_word)

def take_user_input():
  global guesses_remaining
  if guesses_remaining >= 1:
    letter = input("Guess a letter? ")
    if letter.isalpha():
      guess_letter(letter)
    else:
      print("you can only guess letters")
      take_user_input()


def wrong_letter(letter):
  # global guesses_remaining
  print(f"{letter} is not in the word.")
  # print(f"You have {guesses_remaining} guesses remaining.")
  take_user_input()

def update_part_word(letter):
  global part_word

  part_word_list = list(part_word)
  for idx, r in enumerate(random_word):
    if r == letter:
      part_word_list[idx] = letter.upper()
  part_word = "".join(part_word_list)

  pass

def correct_letter(letter):
  update_part_word(letter)
  print(f"{letter.upper()} is in the word {part_word} .")

def guess_word():
  user_input = input("Try and guess the word? ")
  return user_input.lower() == random_word.lower()

# def incorrect_letter():
#   # guess another

def guess_letter(letter):
  global guesses_remaining
  guesses_remaining -= 1
  if guesses_remaining == 0:
    print("you're out of guesses")
    print(f"the word was {random_word}")
  if letter.lower() in random_word:
    correct_letter(letter)
    print(f"You have {guesses_remaining} guesses remaining")
    #prompt to try to guess word
    if guess_word():
      print(f"Congrats, the word was {random_word.upper()}")
    else:
      print("That is not the word.")
      take_user_input()
      # incorrect_letter()
    # if correct, show win message
    # if wrong, prompt to guess another letter
  else:
    wrong_letter(letter)
    print(f"You have {guesses_remaining} guesses remaining")
