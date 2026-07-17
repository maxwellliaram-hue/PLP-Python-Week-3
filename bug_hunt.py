# bug_hunt.py

# BUG: Added the missing closing quotation mark to fix the syntax error.
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: Replaced the text "nmae" with the variable {name} using an f-string.
print(f"Nice to meet you, {name}")

age = input("How old are you? ")

# BUG: Converted age to an integer before adding 1, then displayed the result.
print("Next year you will be", int(age) + 1)
