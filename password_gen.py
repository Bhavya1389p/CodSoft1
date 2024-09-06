import random
import string
def generate_password(length,uppercase=True,lowercase=True, numbers=True,symbols=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
length = int(input("Enter the desired password length: "))
uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
password = generate_password(length,uppercase,lowercase,numbers,symbols)
print("Generated password:", password)