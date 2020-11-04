# Importing 'randint' from 'random'
from random import randint

print("Hello, guess a number between 1 and 10 in 5 tries!")
# Storing a random integer between 1 and 10 in a variable
n = randint(1, 10)

# Allowing 5 prompts max
for i in range(5):
  # Prompting the user for a guess
  guess = int(input("Guess: "))
  # Checking if guess is correct
  if guess == n:
    print("Correct")
    # Break the loop / end the program if "true" before exhausting all 3 chances
    break
  elif guess > n:    
    print("Too big")
  elif guess < n:    
    print("Too small")