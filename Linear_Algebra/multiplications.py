mat1 = [[1, 2, 3], 
        [3, 4, 5]]

mat2 = [[5, 6], 
        [7, 8],
        [9, 10]]

# Function to multiply two matrices
def matrix_multiply(A, B):
  if len(A[0]) != len(B):
    return "Incompatible matrices"
  else:
    result = [[ 0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
      for j in range(len(B[0])):
        sum = 0
        for k in range(len(B)):
          sum += A[i][k] * B[k][j]
        result[i][j] = sum
    return result
# Example usage
print(matrix_multiply(mat1, mat2))
# Output: [[46, 52], 
#          [88, 100]]
