from dataclasses import dataclass
from enum import Enum, auto

# Enum for calculator operations
class Operation(Enum):
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    EXIT = auto()

@dataclass
class Calculator:
    num1: float
    num2: float
    operation: Operation

    def calculate(self) -> float:
        """Perform calculation based on the operation."""
        if self.operation == Operation.ADD:
            return self.num1 + self.num2
        elif self.operation == Operation.SUBTRACT:
            return self.num1 - self.num2
        elif self.operation == Operation.MULTIPLY:
            return self.num1 * self.num2
        elif self.operation == Operation.DIVIDE:
            if self.num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return self.num1 / self.num2
        else:
            raise ValueError("Invalid operation.")



if __name__ == "__main__":
    # This block runs the calculator
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = input("Enter your choice (1-5): ")

            if choice == '5':
                print("Exiting the calculator. Goodbye! 👋")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select from 1-4.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            op_map = {
                '1': Operation.ADD,
                '2': Operation.SUBTRACT,
                '3': Operation.MULTIPLY,
                '4': Operation.DIVIDE
            }
            
            operation = op_map[choice]
            
            # Create a calculator object with user's input
            calculator_instance = Calculator(num1=num1, num2=num2, operation=operation)
            
            # Perform calculation and print result
            result = calculator_instance.calculate()
            print(f"✅ Result: {result}")

        except ValueError:
            print("❌ Error: Invalid input. Please enter valid numbers.")
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")