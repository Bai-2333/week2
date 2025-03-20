def main():
    try:
        # Ask user for input
        grade = input("Enter a numerical grade between 0 - 100: ").strip()

        # Attempt to convert input to integer
        grade = int(grade)

        # Check if grade is within the valid range
        if grade < 0 or grade > 100:
            print("Error: Grades must be between 0 and 100")
            return

        # Determine letter grade
        if 80 <= grade <= 100:
            letter = "A"
        elif 60 <= grade <= 79:
            letter = "B"
        elif 50 <= grade <= 59:
            letter = "C"
        elif 40 <= grade <= 49:
            letter = "D"
        else:
            letter = "F"

        # Print the result
        print(f"Your grade is: {letter}")

    except ValueError:
        print("Error: Please enter a number")

if __name__ == "__main__":
    main()