import numpy as np
import matplotlib.pyplot as plt  # to visualize the matrix at the end

DIMENSION = 3
NB_VECTORS = 100

def generate_random_vectors(n, dim):
    """Generate n random vectors of dimension dim (values between 0 and 1)."""
    return np.random.rand(n, dim)

def cosine_similarity_matrix(vectors):
    """Compute the cosine similarity matrix in a single vectorized operation (much faster)."""
    # Normalize vectors to unit length
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    normalized_vectors = vectors / norms

    # Dot product between all vectors = cosine similarity matrix
    similarity_matrix = normalized_vectors @ normalized_vectors.T

    # Force diagonal to exactly 1.0 (self-similarity)
    np.fill_diagonal(similarity_matrix, 1.0)

    return similarity_matrix

# Generation
vectors = generate_random_vectors(NB_VECTORS, DIMENSION)

# Efficient computation
matrix = cosine_similarity_matrix(vectors)

# Display a small excerpt (the full matrix is 100x100!)
print("5x5 excerpt of the cosine similarity matrix:")
print(matrix[:5, :5].round(4))  # rounded for readability

# Full matrix visualization (heatmap)
plt.figure(figsize=(8, 6))
plt.imshow(matrix, cmap='viridis', vmin=-1, vmax=1)
plt.colorbar(label='Cosine similarity')
plt.title("Cosine similarity matrix (100 random 3D vectors)")
plt.xlabel("Vector index")
plt.ylabel("Vector index")
plt.show()