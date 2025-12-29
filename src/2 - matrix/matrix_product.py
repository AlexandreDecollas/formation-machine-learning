import numpy as np
import matplotlib.pyplot as plt

# Scaling matrix (x2 in X, x3 in Y)
S = np.array([[2, 0],
              [0, 3]])

# Rotation matrix 90° counterclockwise
R = np.array([[0, -1],
              [1, 0]])

# Composition: scaling after rotation
composed = S @ R

print("Scaling S:\n", S)
print("Rotation R:\n", R)
print("Composed (S @ R):\n", composed)

# Apply to basis vectors
v1 = np.array([1, 0])
v2 = np.array([0, 1])

v1_transformed = composed @ v1
v2_transformed = composed @ v2

print("v1 transformed:", v1_transformed)
print("v2 transformed:", v2_transformed)

# Visualization
plt.figure(figsize=(8, 8))
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='v1 original')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v2 original')
plt.quiver(0, 0, v1_transformed[0], v1_transformed[1], angles='xy', scale_units='xy', scale=1, color='orange',
           label='v1 transformed')
plt.quiver(0, 0, v2_transformed[0], v2_transformed[1], angles='xy', scale_units='xy', scale=1, color='green',
           label='v2 transformed')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.grid()
plt.legend()
plt.title("Composition: Scaling after 90° Rotation")
plt.show()
