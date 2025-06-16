from functions import *
import random

word = random.choice(word_generator())
if len(word) > 7:
  attempts = len(word) - 3
else:
  attempts = len(word) - 2
guessed_word = ["_"] * len(word)
print(f"Welcome to Hangman! Your word is {len(word)} characters long. You shall have {attempts} guesses. Use them wisely!")
print(('_ ' * len(word)).strip())


while attempts > 0:
  while True:
    try:
      guess = input("Enter your guess: ").lower()
      if len(guess) != 1 or not ('a' <= guess <= 'z'):
        raise ValueError("Enter a single alphabet letter (a-z)")
      break 
    except ValueError as e:
      print(f"Error raised: {e}")
 
  if guess in word:
    print("Correct Guess!")
    for i in range(len(word)):
      if word[i] == guess:
        guessed_word[i] = guess
  else:
    attempts -= 1
    print(f"Wrong guess! Attempts remaining: {attempts}")

  if "_" not in guessed_word:
    print("\nYou won! The word was: ", word)
    break
  print_word(guessed_word)

else:
  print("\nYou lost. The word was:", word)
    