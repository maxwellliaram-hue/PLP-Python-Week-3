# ticket_checker.py

age = int(input("Enter your age: "))

is_adult = age >= 18

print("Is adult:", is_adult)

if is_adult:
    print("Ticket Price: KSh 500")
else:
    print("Ticket Price: KSh 250")
