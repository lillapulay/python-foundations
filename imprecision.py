x = int(input("x: "))
y = int(input("y: "))

z = x / y
print(f"{z:.30f}")  
# f for formatting, 
# "" for string, 
# {} for plugging in the value of z, not z itself
# :.30 so it prints the value up to 10 decimal places
# last f for the type 'float'

# FLOATING-POINT IMPRECISION
# Inputting 1 and 10 while showing the result with 30 decimal places shows 0.100000000000000005551115123126
# This is due to RAM + bytes / bits: RAM has a finite amount of space, bytes 
# Programming languages decide ahead of time how many bytes/bits to use to represent values in a program
# and if that's not enough, because the program is so big/precise,
# the language will come as close as it can and represent that value with some approximation
# We would need an infinite number of bits to represent an infinite number of numbers precisely

# INTEGER OVERFLOW
# Latest version of Python is designed to use as many bits as it needs to represent integers
# But it is not the case in some languages
# A number too big to fit in the allocated storage: value overflows, where it gets so big that all of the 1s become 0s, so it overflows and starts over
# E.g. allocated space: 3 digits/bits -> 129 turning 130: no issue
# But if 999 -> 1000: no room to fit, so the number gets mistaken for 000

# 2 digits were used to store years - 1999.12.31 scare - could have rolled over to 1900

# Star Wars game: can gather up to 4billion coins - integers are usually stored as 32 bit values ~ roughly 4 billion possible values
# Devs limited the amount of coins to this value so players couldn't cause overflow

# Boeing 747: software bug - power system might turn off while mid-air - turned on 248 days - software counter overflows
# 2 to the 31st power is the number of second in 248 days multiplied by 100
# Temporary workaround was to reboot the plane on the ground before it's on for this long