mat = [[1, 2], 
        [3, 4]]
# Function to calculate the determinant of a square matrix
def determinant(M):
  if len(M) != len(M[0]):
    return "Not a square matrix"
  if len(M) == 2:
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]
  det = 0
  for c in range(len(M)):
    minor = [row[:c] + row[c+1:] for row in M[1:]]
    det += ((-1) ** c) * M[0][c] * determinant(minor)
  return det
# Example usage
print(determinant(mat))
# Output: -2