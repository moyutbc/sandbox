from sympy import Matrix, Symbol, S
from sympy.solvers import solve

if __name__ == '__main__':
    x = Symbol('x')
    y = Symbol('y')
    f1 = x + y
    f2 = x - 1
    ans = solve([f1, f2], [x, y]);
    print(ans)


