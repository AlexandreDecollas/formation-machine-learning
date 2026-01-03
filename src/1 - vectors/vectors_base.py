import numpy as np

# Creation of two vectors
v1 = np.array([3, 4])    # 2D vector
v2 = np.array([1, -2])

# Operations
addition = v1 + v2
scaled = 2.5 * v1  # scalar multiplication

print("v1:", v1)
print("v2:", v2)
print("v1 + v2:", addition)
print("2.5 * v1:", scaled)