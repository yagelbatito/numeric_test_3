from colors import bcolors


def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result

if __name__ == '__main__':

    x_data = [0.35, 0.4, 0.55, 0.65,0.7]
    y_data = [-3.65, -3, -2.6, 0.2,1.67]
    x_interpolate = 0.6  # The x-value where you want to interpolate
    y_interpolate = lagrange_interpolation(x_data, y_data, x_interpolate)
    x1_interpolate = 0.45  # The x-value where you want to interpolate
    y1_interpolate = lagrange_interpolation(x_data, y_data, x1_interpolate)
    print(bcolors.OKBLUE, "\nInterpolated value at x =", x_interpolate, "is y =", y_interpolate, bcolors.ENDC)
    print(bcolors.OKBLUE, "\nInterpolated value at x =", x1_interpolate, "is y =", y1_interpolate, bcolors.ENDC)

    print("https://github.com/yagelbatito/numeric_test_3.git\ngroup:Almog Babila 209477678, Hai karmi 207265678, Yagel Batito 318271863, Meril Hasid 324569714\nstudent:Almog Babila 209477678")