# name_greeter.py

full_name = input("Enter your full name: ").strip()

name_parts = full_name.split()

if len(name_parts) >= 2:
    print(f"Hello, {name_parts[0]}! Welcome.")
else:
    print("Please enter your full name (first and last name).")
