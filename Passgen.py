import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits 

    # generating password here
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# getting length of password
try:
    length = int(input("Enter the desired password length: "))
    if length < 1:
        raise ValueError("Password length must be at least 1")
except ValueError as e:
    print("Invalid input. Please enter a positive integer for password length.")
else:
    password = generate_password(length)
    print("Generated Password:", password)
