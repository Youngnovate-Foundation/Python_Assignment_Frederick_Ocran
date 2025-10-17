import random
import string

# Allow user to specify desired password length
length = int(input("Enter your desired password length: "))

# Allow user to choose whether to include special characters
include_special = input("Include special characters? (yes/no): ").lower()

# Include uppercase letters, lowercase letters, digits and special characters
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
special = string.punctuation

# Randomly generate password
if include_special == "yes":
    characters = upper + lower + digits + special
else:
    characters = upper + lower + digits

password = ''.join(random.choice(characters) for _ in range(length))

# Display the generated password clearly to the user
print("\n Your generated Password is:")
print(password)
