class SimpleCalculator:
    def __init__(self):
        self.operations = {
            '1': self.add,
            '2': self.subtract,
            '3': self.multiply,
            '4': self.divide
        }

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is undefined."
        return a / b

    def menu(self):
        print("\n=== Simple Calculator ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Choose an operation (1-5): ").strip()

            if choice == '5':
                print("Thank you for using the Simple Calculator. Goodbye!")
                break

            if choice not in self.operations:
                print("Invalid choice. Please select a valid operation.")
                continue

            try:
                num1 = float(input("Enter the first number: ").strip())
                num2 = float(input("Enter the second number: ").strip())

                result = self.operations[choice](num1, num2)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator = SimpleCalculator()
    calculator.run()
