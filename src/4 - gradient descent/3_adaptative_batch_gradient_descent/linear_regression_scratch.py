import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data (same as before)
surfaces = np.array([30, 45, 50, 60, 70, 80, 90, 100, 120, 150]).reshape(-1, 1)  # sklearn wants 2D
prices = np.array([170000, 230000, 250000, 290000, 330000, 370000, 410000, 450000, 530000, 650000])

# Your from scratch result (replace with your final w and b)
w_scratch = 4000.0000261567993
b_scratch = 49999.99750751593
# w_scratch = 4000.0   # replace with your final w
# b_scratch = 50000.0  # replace with your final b

# Scikit-learn (2 lines)
model_sk = LinearRegression()
model_sk.fit(surfaces, prices)
w_sk = model_sk.coef_[0]
b_sk = model_sk.intercept_

print(f"From scratch: w = {w_scratch:.2f}, b = {b_scratch:.0f}")
print(f"Scikit-learn: w = {w_sk:.2f}, b = {b_sk:.0f}")

# Prediction lines
pred_scratch = w_scratch * surfaces + b_scratch
pred_sk = model_sk.predict(surfaces)

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(surfaces, prices, color='black', label='Data points')
plt.plot(surfaces, pred_scratch, color='red', linewidth=2, label='From scratch')
plt.plot(surfaces, pred_sk, color='blue', linewidth=2, linestyle='--', label='Scikit-learn')
plt.xlabel("Surface (m²)")
plt.ylabel("Price (€)")
plt.title("Linear Regression: From Scratch vs Scikit-learn")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
