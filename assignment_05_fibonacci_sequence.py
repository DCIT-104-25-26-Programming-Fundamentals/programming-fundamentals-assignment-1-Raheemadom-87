# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
# =============================================================================


def print_fibonacci(n):
    """Prints the first n terms of the Fibonacci sequence."""
    if n <= 0:
        print("Error: Number of terms must be a positive integer.")
        return

    first = 0
    second = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(first, end=" ")
        next_term = first + second
        first = second
        second = next_term

    print()


def is_fibonacci(number):
    """Checks whether a number is in the Fibonacci sequence."""
    if number < 0:
        return False

    first = 0
    second = 1

    while first < number:
        next_term = first + second
        first = second
        second = next_term

    return first == number


def main():
    # Part A
    n = int(input("How many terms? "))
    print_fibonacci(n)

    # Part B
    number = int(input("\nEnter a number to check: "))

    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


# Run the program
main()