import math  # Import the math library for factorial calculation

# Python script to calculate the factorial of a number

def calculate_factorial(number):
    """Calculate the factorial of a number."""
    return math.factorial(number)

# Prompt the user for input
user_input = input("Enter a non-negative integer to calculate its factorial: ")

try:
    # Convert user input to an integer
    number = int(user_input)

    # Check if the number is non-negative
    if number >= 0:
        # Calculate and display the factorial
        factorial_result = calculate_factorial(number)
        print(f"The factorial of {number} is: {factorial_result}")
    else:
        print("Error: Please enter a non-negative integer.")
except ValueError:
    print("Error: Please enter a valid integer.")

