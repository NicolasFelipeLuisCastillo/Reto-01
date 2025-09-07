num1: int = input("Enter the first number: ")
num2: int = input("Enter the second number: ")
operation: str = input("Enter the operation (+, -, *, /): ")


def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        return "Error: Division by zero"


print(calculator(num1, num2, operation))


# Explanation:

# The two numbers and the operation are taken, then the operation to 
# be performed is defined based on the user input. It returns the value of that operation.