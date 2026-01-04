import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

THRESHOLD = 1e-6
INITIAL_LEARNING_RATE = 1e-8
MAX_STEPS = 10000000000
symbol_w, symbol_b, symbol_feature = sp.symbols('w b feature')
f = symbol_w * symbol_feature + symbol_b

surfaces = np.array([30, 45, 50, 60, 70, 80, 90, 100, 120, 150])
prices = np.array([170000, 230000, 250000, 290000, 330000, 370000, 410000, 450000, 530000, 650000])


def adapt_learning_rate(learning_rate, previous_error, new_error):
    if previous_error == float('inf'):
        return learning_rate

    gap = previous_error - new_error
    pourcent_gap = gap / previous_error
    if previous_error < new_error or pourcent_gap >= 0.2:
        return learning_rate / 2
    if pourcent_gap <= 0.1:
        return learning_rate * 2

    return learning_rate


def training():
    w = 0.0
    b = 0.0
    print("Initialization : w:", w, "b:", b)
    recorded_learning_rates = []
    recorded_errors = []

    nb_steps = 0
    learning_rate = INITIAL_LEARNING_RATE
    error = float('inf')
    for steps in range(MAX_STEPS):
        nb_steps+=1
        prediction = w * surfaces + b
        previous_error = error

        error = np.mean((prediction - prices) ** 2)
        recorded_errors.append([nb_steps, error])

        learning_rate = adapt_learning_rate(learning_rate, previous_error, error)
        recorded_learning_rates.append([nb_steps, learning_rate])

        gradient_w = np.mean(2 * (prediction - prices) * surfaces)
        gradient_b = np.mean(2 * (prediction - prices))


        w = w - learning_rate * gradient_w
        b = b - learning_rate * gradient_b

        if nb_steps % 10000 == 0 or error < THRESHOLD:
            print("previous_error: ", previous_error, "error: ",error, "learning_rate: ", learning_rate)
            print(f"∂f/∂w en w={w} : {gradient_w}")
            print(f"∂f/∂b en b={b} : {gradient_b}")
            print(f"Step {nb_steps:2d}: w = {w:.6f}, b = {b:.6f}, error = {error:.10f}")
            print("w:", w, "b:", b, "error:", error, "steps:", nb_steps)

        if error < THRESHOLD:
            break
    print("Converged! w:", w, "b:", b, "nb_steps: ", nb_steps)
    return [recorded_learning_rates, recorded_errors]


def visualize(records):
    """
    Displays the evolution of learning rate and error

    Args:
        records: [learning_rates, errors] where each element is a list of [step, value]
    """
    learning_rates = np.array(records[0])
    errors = np.array(records[1])

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Graph 1: Learning Rate
    ax1.plot(learning_rates[:, 0], learning_rates[:, 1], 'b-', linewidth=1.5)
    ax1.set_xlabel('Steps')
    ax1.set_ylabel('Learning Rate')
    ax1.set_title('Learning Rate Evolution')
    ax1.set_yscale('log')  # Logarithmic scale for Y
    ax1.grid(True, alpha=0.3)

    # Graph 2: Error (MSE)
    ax2.plot(errors[:, 0], errors[:, 1], 'r-', linewidth=1.5)
    ax2.set_xlabel('Steps')
    ax2.set_ylabel('Mean Squared Error')
    ax2.set_title('Error Evolution (MSE)')
    ax2.set_yscale('log')  # Logarithmic scale for Y
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=THRESHOLD, color='g', linestyle='--', label=f'Threshold ({THRESHOLD})')
    ax2.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    records = training()
    visualize(records)
