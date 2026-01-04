import sympy as sp

THRESHOLD = 1e-6
LEARNING_RATE=0.1
MAX_STEPS = 100
symbol_x, symbol_y = sp.symbols('x y')
f = symbol_x ** 2 + symbol_y ** 2
df_dx = sp.diff(f, symbol_x)
df_dy = sp.diff(f, symbol_y)

def main(x, y):
    error = x**2+y**2
    print("Initial error:", error)
    nb_steps=0

    while error > THRESHOLD:
        nb_steps+=1
        print("x:", x, " y:", y)

        gradient_x = float(df_dx.subs(symbol_x, x))
        gradient_y = float(df_dy.subs(symbol_y, y))

        x = x - LEARNING_RATE * gradient_x
        y = y - LEARNING_RATE * gradient_y

        error = x**2 + y**2

        print(f"∂f/∂x en x={x} : {gradient_x}")
        print(f"∂f/∂y en y={y} : {gradient_y}")

        if nb_steps % 5 == 0 or error < THRESHOLD:
            print(f"Step {nb_steps:2d}: x = {x:.6f}, y = {y:.6f}, error = {error:.10f}")

        if error < THRESHOLD:
            print("Converged! x:", x, "y:", y, "error:", error, "steps:", nb_steps)
            break

main(4, 3)
