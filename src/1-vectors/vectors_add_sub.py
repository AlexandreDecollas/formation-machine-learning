import numpy as np
import matplotlib.pyplot as plt

# Two simple 2D vectors
a = np.array([3, 4])   # from origin to (3,4)
b = np.array([1, -2])  # from origin to (1,-2)

# Operations
addition = a + b
subtraction = a - b

print("Vector a:", a)
print("Vector b:", b)
print("a + b =", addition)
print("a - b =", subtraction)

# Quick visualization
plt.figure(figsize=(8, 6))

# Original vectors
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='red', label='a')
plt.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='blue', label='b')

# Addition (green) - rule of the triangle
plt.quiver(0, 0, addition[0], addition[1], angles='xy', scale_units='xy', scale=1, color='green', label='a + b')

# Subtraction (orange) - show -b starting from tip of a
plt.quiver(a[0], a[1], -b[0], -b[1], angles='xy', scale_units='xy', scale=1, color='orange', label='-b (for subtraction)')

plt.xlim(-2, 6)
plt.ylim(-4, 6)
plt.grid()
plt.legend()
plt.title("Vector addition and subtraction")
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.show()