import math
import numpy as np

def cosine_similarity(u, v):
    """Compute cosine similarity between two vectors."""
    dot_product = np.dot(u, v)
    if dot_product == 0:
        return 0
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    return dot_product / (norm_u * norm_v)


a = np.array([1, 0])
b = np.array([0, 1])
c = np.array([2, 0])  # same direction as a, but longer

print(cosine_similarity(a, b))  # → 0.0 (perpendicular)
print(cosine_similarity(a, c))  # → 1.0 (same direction)