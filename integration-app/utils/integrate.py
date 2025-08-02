from sympy import symbols, sympify, integrate, S 

def compute_integral(expression, lower = None, upper=None):
    x = symbols('x')

    expr = sympify(expression)

    if lower is not None and upper is not None:
        result = integrate(expr, (x, lower,upper))
    else:
        result = integrate(expr, x)

    return str(result)