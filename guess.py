import random # This way we import the whole library, not just a certain function

# But that means we need to prefix the function we need with the name of the library
n = random.randint(1, 10)

# Storing the user input in a variable
guess = int(input("Guess: "))

# If guess = n: correct, else: incorrect
# User can try once, then needs to re-run the program
if guess == n:
  print("Correct")
else:  
  print("Incorrect")