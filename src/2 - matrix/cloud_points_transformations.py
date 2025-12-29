import numpy as np
import matplotlib.pyplot as plt

# Define a square: 4 points (clockwise from top-left)
square = np.array([
    [-1, 1],  # top-left
    [1, 1],  # top-right
    [1, -1],  # bottom-right
    [-1, -1]  # bottom-left
])

# Define rotation matrix 45° counterclockwise (use np.pi / 4)
theta = np.pi / 4
counter_clockwise_rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

# Define scaling matrix (x2 in X, x1.5 in Y)
scale_matrix = np.array([
    [2, 0],
    [0, 1.5]
])

# Compose them (scaling after rotation)
scaling_after_rotation = scale_matrix @ counter_clockwise_rotation_matrix

# Compute inverse of the composed matrix
inv_scaling_after_rotation = np.linalg.inv(scaling_after_rotation)

# Apply transformation to square points
transformation = square @ scaling_after_rotation

# Apply inverse to transformed points
inv_transformation = transformation @ inv_scaling_after_rotation
print(inv_transformation)

# Visualization (3 subplots: original, transformed, back to original)
# Use scatter + plot to connect points
# Add titles, grid, axis equal

plt.figure(figsize=(16, 4))

# Original square
plt.subplot(1, 4, 1)
plt.scatter(square[:, 0], square[:, 1], c='blue')
plt.plot(np.append(square[:, 0], square[0, 0]), np.append(square[:, 1], square[0, 1]), 'b-')
plt.title("Original square")
plt.axis('equal')
plt.grid()

# scale_matrix
plt.subplot(1, 4, 2)
plt.scatter(scale_matrix[:, 0], scale_matrix[:, 1], c='orange')
plt.plot(np.append(scale_matrix[:, 0], scale_matrix[0, 0]), np.append(scale_matrix[:, 1], scale_matrix[0, 1]),
         'o-')
plt.title("scale_matrix")
plt.axis('equal')
plt.grid()

# Transformed square
plt.subplot(1, 4, 3)
plt.scatter(transformation[:, 0], transformation[:, 1], c='red')
plt.plot(np.append(transformation[:, 0], transformation[0, 0]), np.append(transformation[:, 1], transformation[0, 1]),
         'r-')
plt.title("Composition: Scaling after 45° Rotation")
plt.axis('equal')
plt.grid()

# Inverse transformed square
plt.subplot(1, 4, 4)
plt.scatter(inv_transformation[:, 0], inv_transformation[:, 1], c='red')
plt.plot(np.append(inv_transformation[:, 0], inv_transformation[0, 0]), np.append(inv_transformation[:, 1], inv_transformation[0, 1]),
         'r-')
plt.title("Inverse transformed square")
plt.axis('equal')
plt.grid()

plt.show()
