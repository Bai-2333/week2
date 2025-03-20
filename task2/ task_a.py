def main():
    # Dictionary mapping days to their corresponding numbers
    days = {
        "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4,
        "Friday": 5, "Saturday": 6, "Sunday": 7
    }

    # Ask user for input
    user_input = input("Enter a day of the week: ").strip().capitalize()

    # Check if the input is a valid day
    if user_input in days:
        print(f"{user_input} is day {days[user_input]}")
    else:
        print("Please enter a valid day")

if __name__ == "__main__":
    main()