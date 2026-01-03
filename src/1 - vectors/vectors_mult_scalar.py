import numpy as np
import matplotlib.pyplot as plt

# Original vector in 2D
a = np.array([1, 3])

# Scalar multiplication (stretching)
scaled = 2 * a

print("Original vector a:", a)
print("a × 2:", scaled)

plt.figure(figsize=(8, 6))

# Original vector (red)
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='red', label='original a')

# Stretched vector (green)
plt.quiver(0, 0, scaled[0], scaled[1], angles='xy', scale_units='xy', scale=1, color='green', label='a × 2')

plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.grid()
plt.legend()
plt.title("Scalar multiplication (stretching)")
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.show()