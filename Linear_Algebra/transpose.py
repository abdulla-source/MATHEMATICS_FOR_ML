mat = [[1, 2, 3], 
       [4, 5, 6]]
# Function to transpose a matrix
def transpose_matrix(M):
  transposed = [[0 for _ in range(len(M))] for _ in range(len(M[0]))]
  for i in range(len(M)):
    for j in range(len(M[0])):
      transposed[j][i] = M[i][j]
  return transposed
# Example usage
print(transpose_matrix(mat))
# Output: [[1, 4], 
#          [2, 5], 
#          [3, 6]]