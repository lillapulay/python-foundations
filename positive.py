def main():
  i = get_positive_int("i: ")
  print(i)

def get_positive_int(prompt):
  while True: # infinite loop
    # Keep prompting the user for an integer
    n = int(input(prompt))
    # Until the user inputs a number greater than 0
    if n > 0:
      # Then stop the loop with break
      break
  # Then returns the value of n  
  return n  

if __name__ == "__main__":
  main()  