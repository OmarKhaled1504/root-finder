import math
import timeit


def bisection(xl, xu, es, imax):
    start = timeit.default_timer()
    iterations = 0
    print("*******Bisection*******")
    if f(xl) * f(xu) >= 0:
        print("Cannot find a root with in the given interval with Bisection")
        return
    else:
        xr = (xl + xu) / 2
        iterationsList = []
        for i in range(imax):
            iterations += 1
            xr = (xl + xu) / 2
            iterationsList.append("Iteration #%d, xr = %.16f and f(xr) = %.16f" % (iterations, xr, f(xr)))
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
        end = timeit.default_timer()

        for iteration in iterationsList:
            print(iteration)
        print("Root = ", xr, "\n# of iterations = ", iterations, "\n Runtime: ", (end - start))


def false_position(xl, xu, es, imax):
    start = timeit.default_timer()
    iterations = 0
    print("******Regula-Falsi******")
    if f(xl) * f(xu) >= 0:
        print("Cannot find a root with in the given interval with Regula-Falsi")
        return
    else:
        xr = xl
        iterationsList = []
        for i in range(imax):
            iterations += 1
            xr = (xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl))
            iterationsList.append("Iteration #%d, xr = %.16f and f(xr) = %.16f" % (iterations, xr, f(xr)))
            if f(xr) == 0 or math.fabs(f(xr)) < es:
                break
            elif f(xr) * f(xu) < 0:
                xu = xr
            else:
                xl = xr
        end = timeit.default_timer()
        for iteration in iterationsList:
            print(iteration)
        print("Root = ", xr, "\n# of iterations = ", iterations, "\n Runtime: ", (end - start))


def secant(xl, xu, es, imax):
    start = timeit.default_timer()
    iterations = 0
    print("********Secant********")
    if f(xl) * f(xu) >= 0:
        print("Cannot find a root with in the given interval with Secant")
    else:
        iterationsList = []
        for i in range(imax):
            iterations += 1

            xr = ((xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl)))
            iterationsList.append("Iteration #%d, xr = %.16f and f(xr) = %.16f" % (iterations, xr, f(xr)))
            test = f(xl) * f(xr)
            xl = xu
            xu = xr
            if test == 0:
                break
            xm = ((xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl)))
            if math.fabs(xm - xr) < es:
                break
        end = timeit.default_timer()
        for iteration in iterationsList:
            print(iteration)
        print("Root = ", xr, "\n# of iterations = ", iterations, "\nRuntime: ", (end - start))


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
