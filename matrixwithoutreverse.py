# Python program to multiply two matrices

# Matrix dimensions
R1 = 1  # Number of rows in Matrix-1
C1 = 6  # Number of columns in Matrix-1
R2 = 6  # Number of rows in Matrix-2
C2 = 32 # Number of columns in Matrix-2

def multiply_matrix(m1, m2):
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(C2)] for _ in range(R1)]

    print("Resultant Matrix is:")

    # Perform the multiplication
    for i in range(R1):
        for j in range(C2):
            for k in range(R2):
                result[i][j] ^= m1[i][k] * m2[k][j]

            print(result[i][j], end="\t")
        print()

# Driver code
if __name__ == "__main__":
    m1 = [[0, 0, 0, 0, 1, 1]]

    m2 = [
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    # Check for dimension compatibility
    if C1 != R2:
        print("The number of columns in Matrix-1 must be equal to the number of rows in Matrix-2")
        print("Please update dimensions accordingly.")
        exit()

    # Function call
    multiply_matrix(m1, m2)
