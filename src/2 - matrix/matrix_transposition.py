import numpy as np

S = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Original matrix S:")
print(S)
print("Transposed matrix St:")
print(S.transpose())
print(S.T)  # Alternative syntax for transpose

print("Transposed inverted:")
print(S.T)