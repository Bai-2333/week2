def is_valid_password(password):
    # Check length requirement
    if len(password) < 8:
        return False

    # Check for at least one letter and one number
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)

    return has_letter and has_number

def main():
    # Ask user for a password
    password = input("Enter a password: ").strip()

    # Validate password
    if is_valid_password(password):
        print("Your password is valid")
    else:
        print("Your password must contain at least 8 characters, and a mix of letters and numbers")

if __name__ == "__main__":
    main()