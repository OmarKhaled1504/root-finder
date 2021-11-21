import math


def bisection(xl, xu, es, imax):
    iterations = 0
    if f(xl) * f(xu) >= 0:
        print("Cannot find a root with in the given interval with Bisection")
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
        print("Cannot find a root with in the given interval with Regula-Falsi")
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


def secant(xl, xu, es, imax):
    iterations = 0
    if f(xl) * f(xu) >= 0:
        print("Cannot find a root with in the given interval with Secant")
    else:
        for i in range(imax):
            iterations += 1
            xr = ((xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl)))
            test = f(xl) * f(xr)
            xl = xu
            xu = xr
            if test == 0:
                break
            xm = ((xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl)))
            if math.fabs(xm - xr) < es:
                break
        print("Root = ", xr, "\n# of iterations = ", iterations)


def f(x):
    return math.exp(-x) - x


if __name__ == '__main__':
    xl = -2
    xu = 4
    es = 0.00001
    imax = 50
    bisection(xl, xu, es, imax)
    false_position(xl, xu, es, imax)
    secant(xl, xu, es, imax)