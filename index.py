import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    """
    Generates a random password based on user preferences.
    """
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase  # Adds uppercase letters (A-Z)
    if use_lower:
        characters += string.ascii_lowercase  # Adds lowercase letters (a-z)
    if use_digits:
        characters += string.digits  # Adds numbers (0-9)
    if use_special:
        characters += string.punctuation  # Adds special characters (!, @, #, etc.)

    # Check if at least one character type is selected
    if not characters:
        return "Error: At least one character type must be selected."

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    try:
        # Get user input
        length = int(input("Enter password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        # Generate and display the password
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number for password length.")

if __name__ == "__main__":
    main()