def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Error: Invalid operation choice"

# Main program
def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Prompt user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt user to choose an operation
    operation = input("Choose an operation (1/2/3/4): ")

    # Perform calculation and display result
    result = calculate(num1, num2, operation)
    print("Result:", result)

# Run the main program
if __name__ == "__main__":
    main()

