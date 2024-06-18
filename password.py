import random
import string

def generate_password(length, include_uppercase=True, include_numbers=True, include_special=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer for the length.")
    include_uppercase = input("Include uppercase letters? ('yes'/'no'): ") == 'yes'
    include_numbers = input("Include numbers? ('yes'/'no'): ") == 'yes'
    include_special = input("Include special characters? ('yes'/'no'): ") == 'yes'
    password = generate_password(length, include_uppercase, include_numbers, include_special)
    print("generated password : ")
    print(password)

if __name__ == "__main__":
    password()
