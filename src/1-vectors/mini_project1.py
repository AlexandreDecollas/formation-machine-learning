## Generate n random 3D vectors and compute their pairwise dot products.

import numpy as np

DIMENSION = 3
NB_VECTORS = 100

def generate_random_vectors(n):
    """Generate n random 3D vectors."""
    return np.random.rand(n, DIMENSION)

def cosine_similarity(u, v):
    dot_product = np.dot(u, v)
    if (dot_product == 0):
        return 0
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    return dot_product / (norm_u * norm_v)


vectors = generate_random_vectors(NB_VECTORS
                                  )
matrix = np.zeros((NB_VECTORS, NB_VECTORS))

for vectorA in range(NB_VECTORS):
    for vectorB in range(NB_VECTORS):
        matrix[vectorA][vectorB] = cosine_similarity(vectors[vectorA], vectors[vectorB])
        print(vectorA, vectorB, matrix[vectorA][vectorB])
