MINIMUM_LENGTH = 2
password = input("Enter a password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password must be at least {MINIMUM_LENGTH} letters long.")
    password = input("Enter a password: ")
    exit()

print("*" * len(password))
