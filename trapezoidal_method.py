import math
import sympy as sp
from sympy.utilities.lambdify import lambdify
from colors import bcolors
from sympy import symbols, diff, sin, cos, tan


def trapezoidal_rule(f, a, b, n,Upper_bound=0):
    g = sp.diff(sp.diff(f))
    g = lambdify(x,g)
    f = lambdify(x,f)
    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    E = (1/12)*(h**2)*(b-a)*g(Upper_bound)
    print("max error is: ",E)

    return integral


if __name__ == '__main__':
    x = sp.symbols('x')
    f = sin((x**2)+ (5*x) +6)/ (2*(math.e ** (-1*x)))
    a = 2.1
    b = 2.6
    n = 400
    result = trapezoidal_rule(f, a, b, n,1)
    print(bcolors.OKBLUE,"Approximate integral:", result, bcolors.ENDC)
    print("https://github.com/yagelbatito/numeric_test_3.git\ngroup:Almog Babila 209477678, Hai karmi 207265678, Yagel Batito 318271863, Meril Hasid 324569714\nstudent:Almog Babila 209477678")