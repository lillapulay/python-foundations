# Importing 'randint' from 'random'
from random import randint

# Storing a random integer between 1 and 10 in a variable
n = randint(1, 10)

# Allowing 3 prompts max
for i in range(3):
  # Prompting the user for a guess
  guess = int(input("Guess: "))
  # Checking if guess is correct
  if guess == n:
    print("Correct")
    # Break the loop / end the program if "true" before exhausting all 3 chances
    break
  else:
    print("Incorrect")