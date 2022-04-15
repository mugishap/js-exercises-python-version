def factorFinder(number):
    factor = []
    for x in range(1, number, 1):
        if number % x == 0:
            factor.append(x)
    return factor


print("The factors are: ", factorFinder(24))
