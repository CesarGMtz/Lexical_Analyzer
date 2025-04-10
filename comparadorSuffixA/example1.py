def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid number, please try again.")

def get_operator():
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("Invalid operator.")

def main():
    print("Simple Calculator")
    while True:
        num1 = get_input("Enter first number: ")
        num2 = get_input("Enter second number: ")
        op = get_operator()

        try:
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)

        again = input("Do you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
