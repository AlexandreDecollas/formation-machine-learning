import sympy as sp

x, y = sp.symbols('x y')
f = x**2 + y**2 + 3*x*y

df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

print("∂f/∂x =", df_dx)  # 2*x + 3*y
print("∂f/∂y =", df_dy)  # 3*x + 2*y