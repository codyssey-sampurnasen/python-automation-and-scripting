"""
Password Generator

Generates a secure random password using letters, numbers, and symbols.

Features:
- Custom length
- Strong random password

Author: Sampurna Sen
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter password length: "))

password = generate_password(length)

print("\nGenerated Password:")
print(password)
