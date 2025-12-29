import numpy as np
import matplotlib.pyplot as plt

# 2x2 rotation matrix: 90 degrees counterclockwise
R = np.array([[0, -1],
              [1,  0]])

# Basis vectors
v1 = np.array([1, 0])  # points right (positive x-axis)
v2 = np.array([0, 1])  # points up (positive y-axis)

# Apply the transformation
v1_rot = R @ v1
v2_rot = R @ v2

# Console output
print("Original v1:", v1)
print("v1 after 90° rotation:", v1_rot)  # → [0, 1]
print("Original v2:", v2)
print("v2 after 90° rotation:", v2_rot)  # → [-1, 0]

# Visualization
plt.figure(figsize=(8, 8))

# Original vectors
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='v1 original (right)')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v2 original (up)')

# Rotated vectors
plt.quiver(0, 0, v1_rot[0], v1_rot[1], angles='xy', scale_units='xy', scale=1, color='orange', label='v1 rotated (up)')
plt.quiver(0, 0, v2_rot[0], v2_rot[1], angles='xy', scale_units='xy', scale=1, color='green', label='v2 rotated (left)')

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.grid()
plt.legend()
plt.title("90° counterclockwise rotation using a 2x2 matrix")
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.show()