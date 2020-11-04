n = int(input("n: "))

# Print hashes as long as i is smaller than n
for i in range(n):  # Range is a built in functionreturning a range of values - goes up to, but not through the value we ask for
  print("#", end="")  # New line (end=) so the hashes won't be printed vertically - end eash line with "nothing" (\n would be a new line)
print()  # After printing hashes, moves the prompt to a new line