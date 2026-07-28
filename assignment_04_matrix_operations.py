# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
# =============================================================================


def read_matrix(rows, cols, name):
    """Reads a matrix from the user."""
    print(f"\nEnter values for {name}:")
    matrix = []

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Please enter exactly {cols} values.")

    return matrix


def display_matrix(matrix):
    """Displays a matrix in a neat grid."""
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


def transpose_matrix(matrix):
    """Returns the transpose of a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


def add_matrices(matrix1, matrix2):
    """Returns the sum of two matrices."""
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    """Returns the product of two matrices."""
    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    cols_b = len(matrix2[0])

    result = []

    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)

    return result


def main():
    # -------------------------
    # Part A: Transpose
    # -------------------------
    print("PART A - Matrix Transpose")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols, "Matrix")

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    print("\nTransposed Matrix:")
    display_matrix(transpose_matrix(matrix))

    # -------------------------
    # Part B: Matrix Addition
    # -------------------------
    print("\nPART B - Matrix Addition")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix1 = read_matrix(rows, cols, "Matrix A")
    matrix2 = read_matrix(rows, cols, "Matrix B")

    print("\nSum of Matrices:")
    display_matrix(add_matrices(matrix1, matrix2))

    # -------------------------
    # Part C: Matrix Multiplication
    # -------------------------
    print("\nPART C - Matrix Multiplication")

    rows_a = int(input("Enter rows of Matrix A: "))
    cols_a = int(input("Enter columns of Matrix A: "))

    matrix_a = read_matrix(rows_a, cols_a, "Matrix A")

    rows_b = int(input("Enter rows of Matrix B: "))
    cols_b = int(input("Enter columns of Matrix B: "))

    if cols_a != rows_b:
        print("Error: Matrix multiplication is not possible.")
        return

    matrix_b = read_matrix(rows_b, cols_b, "Matrix B")

    print("\nProduct of Matrices:")
    display_matrix(multiply_matrices(matrix_a, matrix_b))


# Run the program
main()