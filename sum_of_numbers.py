#!/usr/bin/env python3

# Author: Tony G

# Date: 2025-04-014

# Description: Calculates the sum from 0 up to a number entered by the user (max 100)

def main():
    # Ask the user to enter a number
    user_input_str = input("Enter a positive whole number (up to 100): ")

    try:
        # Try converting input to an integer
        user_input_int = int(user_input_str)

        # Check if number is in valid range
        if user_input_int < 0 or user_input_int > 100:
            print("\nPlease enter a number between 0 and 100.")
        else:
            # Initialize counter and sum
            counter = 0
            total_sum = 0

            # Add numbers from 0 up to the user's number
            while counter < user_input_int:
                counter += 1
                total_sum += counter
                print(f"Counting: {counter}")

            # Display the final result
            print(f"\nThe sum from 0 to {user_input_int} is: {total_sum}")

    except ValueError:
        # If input isn't a valid number
        print("\nInvalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
