import random
import string
def generate_password(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = lower_case + upper_case + digits + special_chars
    if length > len(all_chars):
        print("Error: Password length is too long for the specified complexity.")
        return None
    password = ''.join(random.sample(all_chars, length))
    return password
def main():
    print("Password Generator")

    try:
        password_length = int(input("Enter the desired password length: "))
        generated_password = generate_password(password_length)
        if generated_password:
            print("Generated Password:", generated_password)
    except ValueError:
        print("Invalid input. Please enter a valid password length.")

if __name__ == "__main__":
    main()
