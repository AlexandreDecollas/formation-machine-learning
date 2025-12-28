import numpy as np

a = np.array([2, 3])
b = np.array([1, -2])
c = np.array([4, 6])  # 2 times a

dist_ab = np.linalg.norm(a - b)
dist_ac = np.linalg.norm(a - c)
dist_aa = np.linalg.norm(a - a)

print("Distance a-b:", dist_ab)  # ≈ 5.1
print("Distance a-c:", dist_ac)  # ≈ 5.0 (same direction, different length)
print("Distance a-a:", dist_aa)  # 0.0