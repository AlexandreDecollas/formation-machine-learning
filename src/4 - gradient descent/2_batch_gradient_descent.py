import sympy as sp
import numpy as np

THRESHOLD = 1e-6
LEARNING_RATE = 0.0001
MAX_STEPS = 10000000000
symbol_w, symbol_b, symbol_feature = sp.symbols('w b feature')
f = symbol_w * symbol_feature + symbol_b

surfaces = np.array([30, 45, 50, 60, 70, 80, 90, 100, 120, 150])
prices = np.array([170000, 230000, 250000, 290000, 330000, 370000, 410000, 450000, 530000, 650000])

def training():
    w = 0.0
    b = 0.0
    print("Initialization : w:", w, "b:", b)

    nb_steps = 0
    for steps in range(MAX_STEPS):
        nb_steps+=1
        prediction = w * surfaces + b
        error = np.mean((prediction - prices) ** 2)

        gradient_w = np.mean(2 * (prediction - prices) * surfaces)
        gradient_b = np.mean(2 * (prediction - prices))

        w = w - LEARNING_RATE * gradient_w
        b = b - LEARNING_RATE * gradient_b

        if nb_steps % 10000 == 0 or error < THRESHOLD:
            print(f"∂f/∂w at w={w} : {gradient_w}")
            print(f"∂f/∂b at b={b} : {gradient_b}")
            print(f"Step {nb_steps:2d}: w = {w:.6f}, b = {b:.6f}, error = {error:.10f}")
            print("w:", w, "b:", b, "error:", error, "steps:", nb_steps)

        if error < THRESHOLD:
            break
    print("Converged! w:", w, "b:", b, "nb_steps: ", nb_steps)


training()
