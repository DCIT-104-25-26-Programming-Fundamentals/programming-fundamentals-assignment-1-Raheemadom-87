# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
# =============================================================================


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def exponent(a, b):
    return a ** b


def display_menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        display_menu()

        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Invalid menu choice.")
            continue

        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")

        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")

        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")

        elif choice == "4":
            result = divide(num1, num2)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {num1} / {num2} = {result:.2f}")

        elif choice == "5":
            result = modulus(num1, num2)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {num1} % {num2} = {result}")

        elif choice == "6":
            result = exponent(num1, num2)
            print(f"Result: {num1} ** {num2} = {result}")


# Run the program
main()