class Calculator:
    def __init__(self):
        self.running = True

    def run(self):
        print("Welcome to the OOP Calculator!")
        while self.running:
            self.perform_calculation()
            self.ask_continue()

    def perform_calculation(self):
        try:
            a = self.get_number("First number: ")
            b = self.get_number("Second number: ")
            operation = self.get_operation()

            result = self.calculate(a, b, operation)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def get_operation(self):
        operations = {'+': self.add, '-': self.subtract, '*': self.multiply, '/': self.divide}
        while True:
            op = input("Choose operation (+, -, *, /): ")
            if op in operations:
                return operations[op]
            print("Invalid operation.")

    def calculate(self, x, y, operation):
        return operation(x, y)

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def ask_continue(self):
        response = input("Continue? (y/n): ").strip().lower()
        if response != 'y':
            self.running = False
            print("Exiting...")

if __name__ == "__main__":
    app = Calculator()
    app.run()
