import jacobi_utilities
from sympy import *
import numpy as np
from math import pi

x = Symbol('x')

def my_natural_cubic_spline(f,x0,clamped = 0):
    n = (len(f)-1)*4
    numOfPolynoms = len(f)-1
    vector = np.zeros(n)
    mat = np.zeros((n,n))
    row = 0
    #first (2 * number of polinoms) lines of mat
    for i in range(len(f)-1):
        strong = 3
        for j in range(i*4,(i+1)*4):
            mat[row][j] = f[i][0]**strong
            mat[row+1][j] = f[i+1][0]**strong
            strong = strong - 1
        row = row + 2

    #next (number of polinoms - 1) lines
    rows = []
    for row in range(2 * numOfPolynoms, (2 * numOfPolynoms) + (numOfPolynoms - 1)):
        rows.append(row)
    for i in range(1,len(f)-1):
        strong = 2
        mul = 3
        for j in range((i-1)*4,(i*4)-1):
            mat[rows[i-1]][j] = -((f[i][0]**strong) * mul)
            mat[rows[i-1]][j+4] = (f[i][0]**strong) * mul
            strong = strong - 1
            mul = mul - 1

    rows = []
    for row in range((2 * numOfPolynoms) + (numOfPolynoms - 1),(2 * numOfPolynoms) + (2 * (numOfPolynoms - 1))):
        rows.append(row)
    for i in range(1,len(f)-1):
        strong = 1
        mul = 6
        for j in range((i-1)*4,(i*4)-2):
            mat[rows[i - 1]][j] = -((f[i][0] ** strong) * mul)
            mat[rows[i - 1]][j + 4] = (f[i][0] ** strong) * mul
            strong = strong - 1
            mul = mul / 3

    rows = []
    for row in range((2 * numOfPolynoms) + (2*(numOfPolynoms - 1)), (2 * numOfPolynoms) + (2 * (numOfPolynoms - 1) + 2)):
        rows.append(row)

    if clamped == 0:
        mat[rows[0]][0] = 6 * f[0][0]
        mat[rows[0]][1] = 2
        mat[rows[1]][n-4] = 6 * f[numOfPolynoms][0]
        mat[rows[1]][n-3] = 2

    else:
        mat[rows[0]][0] = 3
        mat[rows[0]][1] = 2
        mat[rows[0]][2] = 1
        mat[rows[1]][n - 4] = 3 * (f[numOfPolynoms][0] ** 2)
        mat[rows[1]][n - 3] = 2 * f[numOfPolynoms][0]
        mat[rows[1]][n - 2] = 1


    for i in range(numOfPolynoms):
        vector[i*2] = f[i][1]
        vector[i*2+1] = f[i+1][1]
    if clamped != 0:
        vector[n-2] = clamped[0][1]
        vector[n-1] = clamped[1][1]

    solution = np.linalg.solve(mat, vector)

    for i in range(1,numOfPolynoms+1):
        if x0 < f[i][0] and x0 > f[i-1][0]:
            y = solution[(i*4)-1] + (solution[(i*4)-2] * x0) + (solution[(i*4)-3] * (x0 ** 2)) + (solution[(i*4)-4] * (x0 ** 3))

    print(mat)
    return y



if __name__ == '__main__':
    f = [(0, 0), (pi/6, 0.5), (pi/4, 0.7072), (pi/2, 1)]
    x0 = pi/3
    g = [(0, 1), (pi/2, 0)]

    print("func: " + str(f))
    print("x0 = " + str(x0) + "\n")
    print(my_natural_cubic_spline(f, x0, g))
    print("https://github.com/Babilabong/tester_3_nomarit\ngroup:Almog Babila 209477678, Hai karmi 207265678, Yagel Batito 318271863, Meril Hasid 324569714\nstudent:Almog Babila 209477678")