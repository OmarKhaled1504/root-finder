import math
import timeit


def bisection(xl, xu, es=0.00001, imax=50):
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
            ea = math.fabs((xu - xl) / xl)
            iterationsList.append(
                "Iteration #%d, xr = %.16f, f(xr) = %.16f and precision: %.16f " % (iterations, xr, f(xr), ea))
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
        print("Root = ", xr, "Precision: ", ea, "\n# of iterations = ", iterations, "\nRuntime: ", (end - start))
    return xr, ea, iterations, iterationsList, (end - start)


def false_position(xl, xu, es=0.00001, imax=50):
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
            ea = math.fabs(f(xr))
            iterationsList.append(
                "Iteration #%d, xr = %.16f, f(xr) = %.16f and precision: %.16f " % (iterations, xr, f(xr), ea))
            if f(xr) == 0 or ea < es:
                break
            elif f(xr) * f(xu) < 0:
                xu = xr
            else:
                xl = xr
        end = timeit.default_timer()
        for iteration in iterationsList:
            print(iteration)
        print("Root = ", xr, "Precision: ", ea, "\n# of iterations = ", iterations, "\nRuntime: ", (end - start))
    return xr, ea, iterations, iterationsList, (end - start)


def secant(xl, xu, es=0.00001, imax=50):
    start = timeit.default_timer()
    iterations = 0
    print("********Secant********")
    if f(xl) * f(xu) >= 0:
        print("Cannot find a root with in the given interval with Secant")
        return
    else:
        iterationsList = []
        for i in range(imax):
            iterations += 1

            xr = ((xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl)))
            test = f(xl) * f(xr)
            xl = xu
            xu = xr
            if test == 0:
                break
            xm = ((xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl)))
            ea = math.fabs(xm - xr)
            iterationsList.append(
                "Iteration #%d, xr = %.16f, f(xr) = %.16f and precision: %.16f " % (iterations, xr, f(xr), ea))
            if ea < es:
                break
        end = timeit.default_timer()
        for iteration in iterationsList:
            print(iteration)
        print("Root = ", xr, "Precision: ", ea, "\n# of iterations = ", iterations, "\nRuntime: ", (end - start))
    return xr, ea, iterations, iterationsList, (end - start)


def fixed_point(xi, es=0.00001, imax=50):
    start = timeit.default_timer()
    iterations = 0
    print("*******Fixed point*******")
    x = xi
    iterationsList = []
    for i in range(imax):
        iterations += 1
        xp = x
        x = g(x)

        ea = abs((x - xp) / x) * 100
        iterationsList.append(
            "Iteration #%d, x = %.16f, f(x) = %.16f and precision: %.16f " % (iterations, x, f(x), ea))
        if ea < es:
            break
    end = timeit.default_timer()
    for iteration in iterationsList:
        print(iteration)
    print("Root = ", x, "Precision: ", ea, "\n# of iterations = ", iterations, "\nRuntime: ", (end - start))
    return x, ea, iterations, iterationsList, (end - start)


def newton_raphson(xi, es=0.00001, imax=50):
    start = timeit.default_timer()
    iterations = 0
    print("*******Newton Raphson*******")
    x = xi
    iterationsList = []
    for i in range(imax):
        iterations += 1
        fx = f(x)

        xp = x
        x = x - (fx / derivative(x))
        ea = abs((x - xp) / x) * 100
        iterationsList.append(
            "Iteration #%d, x = %.16f, f(x) = %.16f and precision: %.16f " % (iterations, x, f(x), ea))
        if ea < es:
            break
    end = timeit.default_timer()
    for iteration in iterationsList:
        print(iteration)
    print("Root = ", x, "Precision: ", ea, "\n# of iterations = ", iterations, "\nRuntime: ", (end - start))
    return x, ea, iterations, iterationsList, (end - start)


def f(x):
    return math.e ** -x - x


def g(x):
    return math.e ** -x


def derivative(x, dx=1e-6):
    df = f(x + dx) - f(x - dx)
    return df / (2 * dx)


if __name__ == '__main__':
    xl = -2
    xu = 4
    xi = 0.5
    bisection(xl, xu)
    false_position(xl, xu)
    secant(xl, xu)
    newton_raphson(xi)
    fixed_point(xi)
