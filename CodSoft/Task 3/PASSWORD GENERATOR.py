import random
import string

def generate_password(length):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one character from each character set
    password = [random.choice(string.ascii_lowercase),
                random.choice(string.ascii_uppercase),
                random.choice(string.digits),
                random.choice(string.punctuation)]

    # Fill the rest of the password with random characters
    password.extend(random.choice(characters) for _ in range(length - 4))

    # Shuffle the characters to make it more random
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length must be at least 4 characters.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid integer for the password length.")
