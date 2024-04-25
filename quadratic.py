# Replace the "ANSWER HERE" for your answer
import math
def roots(a, b, c):
    discriminante = math.pow(b, 2) - 4 * a * c
    if discriminante < 0:
        return "( )"
    elif discriminante == 0: 
        return f"({-b/(2*a)})"
    else: 
        return f"({(-b + math.sqrt(discriminante))/2*a}, {(-b - math.sqrt(discriminante))/2*a})"

def value_y(a, b, c, x):
        return a*x**2 + b*x + c


def to_string(a, b, c):
    if a == 0:
        return f"f(x) = {b}x + {c}" 
    if b == 0:
        return f"f(x) = {a}x^2 + {c}"
    if c == 0: 
        return f"f(x) = {a}x^2 + {b} * X"
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    else: 
        return f"f(x) = {a}x^2 + {b}x + {c}"

def derivation(a, b, c):
    if a*2 == 0:
        return f"f'(x) = {b}"
    if b == 0:
        return f"f'(x) = {a*2} * X"
    return f"f'(x) = {a*2} * X + {b}"


#print(roots(1, -3, 2)) # Retorna: "(2.0, 1.0)"
#print(roots(1, -2, 1)) # Retorna: "(1.0)"
#print(roots(1, 2, 3))  # Retorna: "( )"

#print(value_y(1, -3, 2, 0)) # Retorna: 2
#print(value_y(1, -3, 2, 1)) # Retorna: 0
#print(value_y(1, -3, 2, -1)) # Retorna: 6

#print(to_string(2, -3, 1)) # Retorna: "f(x) = 2 * X^2 + -3 * X + 1"

#print(derivation(2, -3)) # Retorna: "f'(x) = 4x + -3"
