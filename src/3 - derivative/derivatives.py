import numpy as np
import matplotlib.pyplot as plt

# Function f(x) = x²
def f(x):
    return x**2

# Derivative f'(x) = 2x (analytical)
def df(x):
    return 2 * x

# Numerical approximation of derivative (for understanding)
def numerical_derivative(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

# Values to evaluate
x_values = np.linspace(-3, 3, 100)

# Plot function and derivative
plt.figure(figsize=(8, 6))
plt.plot(x_values, f(x_values), label='f(x) = x²', color='blue')
plt.plot(x_values, df(x_values), label="f'(x) = 2x", color='red', linestyle='--')
plt.scatter([0, 1, 2], [f(0), f(1), f(2)], color='blue', zorder=5)
plt.scatter([0, 1, 2], [df(0), df(1), df(2)], color='red', zorder=5)
plt.title("Function and its derivative")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

# Check numerical vs analytical at x=2
print("Analytical derivative at x=2:", df(2))
print("Numerical derivative at x=2:", numerical_derivative(f, 2))