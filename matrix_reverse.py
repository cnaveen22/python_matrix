# Define matrices A and B
A = [
    [0],
    [0],
    [0],           
    [0],
    [1],
    [1]
]


B = [
    [1, 0, 0, 0, 0, 0],   
    [1, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 1, 0], 
    [1, 0, 0, 0, 1, 1], 
    [1, 0, 0, 1, 0, 0], 
    [1, 0, 0, 1, 0, 1], 
    [1, 0, 0, 1, 1, 0], 
    [1, 0, 0, 1, 1, 1], 
    [1, 0, 1, 0, 0, 0], 
    [1, 0, 1, 0, 0, 1], 
    [1, 0, 1, 0, 1, 0], 
    [1, 0, 1, 0, 1, 1], 
    [1, 0, 1, 1, 0, 0], 
    [1, 0, 1, 1, 0, 1], 
    [1, 0, 1, 1, 1, 0], 
    [1, 0, 1, 1, 1, 1], 
    [1, 1, 0, 0, 0, 0], 
    [1, 1, 0, 0, 0, 1], 
    [1, 1, 0, 0, 1, 0], 
    [1, 1, 0, 0, 1, 1], 
    [1, 1, 0, 1, 0, 0], 
    [1, 1, 0, 1, 0, 1], 
    [1, 1, 0, 1, 1, 0], 
    [1, 1, 0, 1, 1, 1], 
    [1, 1, 1, 0, 0, 0], 
    [1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0], 
    [1, 1, 1, 0, 1, 1], 
    [1, 1, 1, 1, 0, 0], 
    [1, 1, 1, 1, 0, 1], 
    [1, 1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1, 1]
]

# Function to perform binary matrix multiplication
def binary_matrix_multiply(A, B):
    # Get dimensions
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if multiplication is possible
    if cols_A != rows_B:
        return None

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform binary matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] ^= (A[i][k] & B[k][j])  # XOR for binary addition, AND for multiplication

    return result

# Perform the multiplication if possible
result_AB = binary_matrix_multiply(A, B)
if result_AB:
    print("Result of A x B:")
    for row in result_AB:
        print(row)
else:
    print("Matrix multiplication A x B is not possible due to incompatible dimensions.")

result_BA = binary_matrix_multiply(B, A)
if result_BA:
    print("Result of B x A:")
    for row in result_BA:
        print(row)
else:
    print("Matrix multiplication B x A is not possible due to incompatible dimensions.")
