import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt the user for the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        
        # Ensure the length is positive
        if length <= 0:
            print("Please enter a positive integer for the password length.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
