"""
https://github.com/Babilabong/analiza-nomarit/blob/main/task3/main.py
"""

import sympy as sp
from sympy import *
from sympy.utilities.lambdify import lambdify

def newton_raphson(func, a, b, eps=1e-4):
    h = sp.diff(func)
    func = lambdify(x,func)
    h = lambdify(x,h)
    xr = (a+b)/2
    result_newton.append(xr)
    while(abs(func(xr)) > eps):
        xr = xr - (func(xr)/h(xr))
        result_newton.append(xr)
        if xr < a or xr > b:
            raise Exception("out of range")
        if len(result_newton)>maxIter:
            raise Exception("too many iterations")

    return len(result_newton)

def meitar(func, a, b, eps=1e-4):
    func = lambdify(x, func)
    result_meitar.append(a)
    result_meitar.append(b)
    counter = 1
    while(abs(func(result_meitar[counter]))>eps):
        lastX = (result_meitar[counter-1]*func(result_meitar[counter])-result_meitar[counter]*func(result_meitar[counter-1]))/(func(result_meitar[counter])-func(result_meitar[counter-1]))
        if lastX < a or lastX > b:
            raise Exception("out of range")
        if len(result_meitar)>maxIter:
            raise Exception("too many iterations")
        result_meitar.append(lastX)
        counter = counter + 1

    return len(result_meitar)

maxIter = 1000
result_newton = []
result_meitar = []
x = sp.symbols('x')
f = 4*(x**3) - (48*x)+5
a = 3
b = 4
try:
    newtonIter = newton_raphson(f,a,b)
    meitarIter = meitar(f,a,b)
    print("Newton raphson method:")
    print(f"the input is: \nfunction:{f},range:{a} -> {b}")
    print("The result list is: ", result_newton)
    print("The iteration number is: ",newtonIter)
    print("the root is: ",result_newton[newtonIter-1])
    print()
    print("meitar method:")
    print(f"the input is: \nfunction:{f},range:{a} -> {b}")
    print("The result list is: ", result_meitar)
    print("The iteration number is: ", meitarIter)
    print("the root is: ", result_meitar[meitarIter - 1])
except Exception as e:
    print(e)