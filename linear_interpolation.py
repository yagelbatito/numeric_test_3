from colors import bcolors


def linearInterpolation(table_points, point):
    p = []
    result = 0
    flag = 1
    for i in range(len(table_points)):
        p.append(table_points[i][0])
    for i in range(len(p) - 1):
        if table_points[i][0] <= point <= table_points[i + 1][0]:
            x1 = table_points[i][0]
            x2 = table_points[i + 1][0]
            y1 = table_points[i][1]
            y2 = table_points[i + 1][1]
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print(bcolors.OKGREEN, "\nThe approximation (interpolation) of the point ", point, " is: ",bcolors.ENDC, round(result, 4))
            flag = 0
    if flag:
        if point < p[0]:
            a = 0
            b = 1
        else:
            a = len(p)-2
            b = a + 1
        x1 = table_points[a][0]
        x2 = table_points[b][0]
        y1 = table_points[a][1]
        y2 = table_points[b][1]
        m = (y1 - y2) / (x1 - x2)
        result = y1 + m * (point - x1)
        print(bcolors.OKGREEN, "\nThe approximation (extrapolation) of the point ", point, " is: ",bcolors.ENDC, round(result, 4))


if __name__ == '__main__':

    table_points = [(1, 3), (2, 4), (3, -1)]
    x = 1.5
    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x)
    linearInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)
    print("https://github.com/Babilabong/tester_3_nomarit\ngroup:Almog Babila 209477678, Hai karmi 207265678, Yagel Batito 318271863, Meril Hasid 324569714\nstudent:Almog Babila 209477678")