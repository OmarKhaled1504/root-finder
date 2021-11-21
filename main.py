import math


def bisection(xl, xu, es, imax):
    iterations = 0
    if f(xl) * f(xu) > 0:
        print("Not solvable with bisection")
        return
    xr = (xl + xu) / 2
    for i in range(imax):
        iterations += 1
        xr = (xl + xu) / 2
        ea = math.fabs((xu - xl) / xl)
        test = f(xl) * f(xr)
        if test < 0:
            xu = xr
        else:
            xl = xr
        if test == 0:
            ea = 0
        if ea < es:
            break
    print("Root = ", xr, "\n# of iterations = ", iterations)


def false_position(xl, xu, es, imax):
    iterations = 0
    if f(xl) * f(xu) >= 0:
        print("Not solvable with regula-falsi")
        return
    xr = xl
    for i in range(imax):
        iterations += 1
        xr = (xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl))
        if f(xr) == 0 or math.fabs(f(xr)) < es:
            break
        elif f(xr) * f(xu) < 0:
            xu = xr
        else:
            xl = xr

    print("Root = ", xr, "\n# of iterations = ", iterations)


def f(x):
    return math.exp(-x) - x


if __name__ == '__main__':
    bisection(-2, 4, 0.00001, 50)
    false_position(-2, 4, 0.00001, 50)
