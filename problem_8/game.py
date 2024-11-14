import random

guesses_remaining = 5
letter = ""
part_word = ""
random_word = ""
word_guessed = False

def greeting():
  print("Let's Play Hangman ¯\\_(ツ)_/¯")

def create_part_word():
  """Create 'word' made of underscores"""
  global part_word
  temp = []
  for r in random_word:
    temp.append("_")
  part_word = "".join(temp)

def choose_word():
  """Chose a random word for the user to try to guess"""
  f_handle = open(f'./problem_8/common_words.txt','r').read()
  words = f_handle.strip().split("\n")
  random_index = random.randint(0, len(words) - 1)
  return words[random_index]

random_word = choose_word()
print(random_word)

def take_user_input():
  """Prompt user to guess a letter"""
  global guesses_remaining
  if guesses_remaining >= 1:
    letter = input("Guess a letter? ")
    if letter.isalpha() and len(letter) == 1:
      guess_letter(letter)
    else:
      print("you can only guess letters, and only one at a time please")
      take_user_input()

def wrong_letter(letter):
  """Tell the user their guess was wrong, and prompt them to guess again"""
  print(f"{letter} is not in the word.")

def update_part_word(letter):
  """Update underscores to replace correctly guessed letters"""
  global part_word

  part_word_list = list(part_word)
  for idx, r in enumerate(random_word):
    if r == letter:
      part_word_list[idx] = letter.upper()
  part_word = "".join(part_word_list)

def correct_letter(letter):
  """Tell user their guess is correct, and show them new 'part word'"""
  update_part_word(letter)
  print(f"{letter.upper()} is in the word {part_word} .")

def guess_word():
  """Take user's word guess and checks if it is correct"""
  user_input = input("Try and guess the word? ")
  return user_input.lower() == random_word.lower()

def guess_letter(letter):
  """takes user's letter guess and provides feedback"""
  global guesses_remaining
  global word_guessed
  # if correct letter guessed, give them a chance to guess the word
  # if word or letter incorrect, then decrement remaning guesses and prompt again
  if letter.lower() in random_word:
    correct_letter(letter)
    if guess_word():
      print(f"Congrats, the word was {random_word.upper()}")
      word_guessed = True
    else:
      print("That is not the word.")
  else:
      wrong_letter(letter)

  guesses_remaining -= 1
 
  if not word_guessed :
    # if no guesses remaining, then reveal the word, otherwise remind them how many guesses remain
    if guesses_remaining == 0:
      print("you're out of guesses")
      print(f"the word was {random_word.upper()}")
    else:
      print(f"You have {guesses_remaining} guesses remaining")
      take_user_input()
