x = int(input("x: "))
y = int(input("y: "))

if x < y:
  print("x is less than y")
elif x > y: # Python uses elif instead of else if
  print("x is greater than y")
# elif x == y: # Equality operator, a single = is for assigning values 
# But logically the only option here is that the values are equal, so else is enough
else:
  print("x equals y")
# Colon after condition: do the following, if the condition is true
# Indentation matters in python!