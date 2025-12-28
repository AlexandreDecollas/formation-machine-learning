import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([2, 3])
v2 = np.array([1, -2])

dot_product = v1 @ v2
print("Dot product v1 . v2 =", dot_product)  # -4

# Compute the projection of v1 onto v2 (for visualization)
norm_v2 = np.linalg.norm(v2)
projection_scalar = dot_product / (norm_v2 ** 2)  # Correct scalar for orthogonal projection
projection_vector = projection_scalar * v2  # Projection vector

plt.figure(figsize=(10, 8))

# Original vectors
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='red', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v2')

# Projection of v1 onto v2 (dashed line)
plt.quiver(0, 0, projection_vector[0], projection_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='green', linestyle='dashed', label='Projection of v1 onto v2')

# Perpendicular line from v1 tip to projection (commented to avoid dash bug if needed)
# plt.plot([v1[0], projection_vector[0]], [v1[1], projection_vector[1]], 'k:', alpha=0.7)

plt.xlim(-3, 4)
plt.ylim(-4, 4)
plt.grid()
plt.legend()
plt.title(f"Dot product = {dot_product} (negative → obtuse angle)")
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.show()