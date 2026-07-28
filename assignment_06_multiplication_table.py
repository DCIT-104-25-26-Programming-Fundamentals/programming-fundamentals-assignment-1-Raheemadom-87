# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
# =============================================================================


def print_table(number):
    """Prints the multiplication table for a single number."""
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


def print_tables(n):
    """Prints multiplication tables from 1 to n."""
    if n <= 0:
        print("Error: Number must be a positive integer.")
        return

    for number in range(1, n + 1):
        print_table(number)
        print("-" * 30)


def main():
    # Part A
    number = int(input("Enter a number: "))
    print_table(number)

    # Part B
    n = int(input("\nEnter a number (N): "))

    if n <= 0:
        print("Error: Number must be a positive integer.")
        return

    print_tables(n)


# Run the program
main()