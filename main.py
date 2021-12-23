import timeit
import Global
import math
from math import sin, cos, tan, log


def bisection(xl, xu, es, imax):
    if(es == ''):
        es= 0.00001
    if(imax == ''):
        imax = 50
    start = timeit.default_timer()
    iterations = 0
    ea = 0
    print("*******Bisection*******")
    if f(xl) * f(xu) >= 0:
        print("Cannot find a root with in the given interval with Bisection")
        return
    else:
        xr = (xl + xu) / 2
        iterationsList = []
        prev = 0
        for i in range(imax):
            iterations += 1
            xr = (xl + xu) / 2
            try:
                ea = math.fabs((xr - prev) / xr)
                prev = xr
            except ZeroDivisionError:
                print("division by zero!")
                break
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


def false_position(xl, xu, es, imax):
    if (es == ''):
        es = 0.00001
    if (imax == ''):
        imax = 50
    start = timeit.default_timer()
    iterations = 0
    ea = 0
    print("******Regula-Falsi******")

    if f(xl) * f(xu) >= 0:
        print("Cannot find a root with in the given interval with Regula-Falsi")
        return
    else:
        xr = xl
        iterationsList = []
        prev = 0
        for i in range(imax):
            iterations += 1
            try:
                xr = (xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl))
            except ZeroDivisionError:
                print("division by zero!")
                break

            try:
                ea = math.fabs((xr - prev) / xr)
                prev = xr
            except ZeroDivisionError:
                print("division by zero!")
                break
            iterationsList.append(
                "Iteration #%d, xr = %.16f, f(xr) = %.16f and precision: %.16f " % (iterations, xr, f(xr), ea))
            if f(xr) == 0 or ea < es:
                break
            elif f(xr) < 0:
                xu = xr
            else:
                xl = xr
        end = timeit.default_timer()
        for iteration in iterationsList:
            print(iteration)
        print("Root = ", xr, "Precision: ", ea, "\n# of iterations = ", iterations, "\nRuntime: ", (end - start))
    return xr, ea, iterations, iterationsList, (end - start)


def secant(xl, xu, es, imax):
    if (es == ''):
        es = 0.00001
    if (imax == ''):
        imax = 50
    start = timeit.default_timer()
    iterations = 0
    ea = 0
    print("********Secant********")

    iterationsList = []
    prev = 0
    for i in range(imax):
        iterations += 1
        try:
            xr = xl - (f(xl) * (xu - xl) / (f(xu) - f(xl)))
        except ZeroDivisionError:
            print("division by zero!")
            break
        xl = xu
        xu = xr
        try:
            ea = math.fabs((xr - prev) / xr)
            prev = xr
        except ZeroDivisionError:
            print("division by zero!")
            break
        iterationsList.append(
            "Iteration #%d, xr = %.16f, f(xr) = %.16f and precision: %.16f " % (iterations, xr, f(xr), ea))

        if ea < es:
            break
        if ea < es:
            break
    end = timeit.default_timer()
    for iteration in iterationsList:
        print(iteration)
    print("Root = ", xr, "Precision: ", ea, "\n# of iterations = ", iterations, "\nRuntime: ", (end - start))


    return xr, ea, iterations, iterationsList, (end - start)


def fixed_point(xi, es, imax):
    if (es == ''):
        es = 0.00001
    if (imax == ''):
        imax = 50
    start = timeit.default_timer()
    iterations = 0
    ea = 0
    print("*******Fixed point*******")
    x = xi
    iterationsList = []
    for i in range(imax):
        iterations += 1
        xp = x
        x = f(x)
        try:
            ea = abs((x - xp) / x)
        except ZeroDivisionError:
            print("division by zero!")
            break
        iterationsList.append(
            "Iteration #%d, x = %.16f, f(x) = %.16f and precision: %.16f " % (iterations, x, f(x), ea))
        if ea < es:
            break
    end = timeit.default_timer()
    for iteration in iterationsList:
        print(iteration)
    print("Root = ", x, "Precision: ", ea, "\n# of iterations = ", iterations, "\nRuntime: ", (end - start))
    return x, ea, iterations, iterationsList, (end - start)


def newton_raphson(xi, es, imax):
    if (es == ''):
        es = 0.00001
    if (imax == ''):
        imax = 50
    start = timeit.default_timer()
    iterations = 0
    print("*******Newton Raphson*******")
    x = xi
    iterationsList = []
    ea = 0
    for i in range(imax):
        iterations += 1
        fx = f(x)

        xp = x
        try:
            x = x - (fx / derivative(x))
        except ZeroDivisionError:
            print("division by zero!")
            break
        try:
            ea = abs((x - xp) / x)
        except ZeroDivisionError:
            print("division by zero!")
            break
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
    function = Global.EQN
    function = function.replace('ln', 'log')
    function = function.replace('^', '**')
    function = function.replace('e', 'math.e')
    function = function.replace('pi','math.pi')
    return eval(function)




def derivative(x, dx=1e-6):
    df = f(x + dx) - f(x - dx)
    return df / (2 * dx)
