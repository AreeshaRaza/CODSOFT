def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y
def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    while True:
        try:
            choice = int(input("Enter operation choice (1/2/3/4): "))
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select a valid operation.")
                continue
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == 4:
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

        again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
