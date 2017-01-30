from sympy import solve, symbols

x = symbols('x')
a = solve([x**2 - 2.001],[x])
print(a)
