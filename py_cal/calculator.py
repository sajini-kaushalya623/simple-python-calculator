"""
Simple Calculator Program
A beginner-friendly calculator that performs basic arithmetic operations.
Created for learning purposes.
"""

# Function to add two numbers
def add(num1, num2):
    """Add two numbers and return the result."""
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    """Subtract num2 from num1 and return the result."""
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    """Multiply two numbers and return the result."""
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    """Divide num1 by num2 and return the result. Handles division by zero."""
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2

# Function to display the menu
def display_menu():
    """Display the calculator menu with available operations."""
    print("\n" + "="*50)
    print("        SIMPLE CALCULATOR")
    print("="*50)
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("-"*50)

# Function to get valid number input from user
def get_number_input(prompt):
    """Get a valid number from the user with error handling."""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Function to get operation choice from user
def get_operation_choice():
    """Get a valid operation choice from user (1-5)."""
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("❌ Invalid choice! Please select a number from 1 to 5.")

# Main calculator function
def calculator():
    """Main function that runs the calculator program."""
    print("\n🎉 Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        choice = get_operation_choice()
        
        if choice == '5':
            print("\n👋 Thank you for using the calculator!")
            print("Goodbye! 🎉\n")
            break
        
        print("\nEnter two numbers:")
        num1 = get_number_input("First number: ")
        num2 = get_number_input("Second number: ")
        
        print("\n" + "="*50)
        
        if choice == '1':
            result = add(num1, num2)
            print(f"✅ Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"✅ Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"✅ Result: {num1} × {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(f"❌ {result}")
            else:
                print(f"✅ Result: {num1} ÷ {num2} = {result}")
        
        print("="*50)
        
        continue_choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_choice not in ['yes', 'y']:
            print("\n👋 Thank you for using the calculator!")
            print("Goodbye! 🎉\n")
            break

# Entry point of the program
if __name__ == "__main__":
    calculator()