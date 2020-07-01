def disyuncion(x1, x2):
    if abs(x1) > abs(x2):
        return x1

    return x2


def conjuncion(x1, x2):
    if abs(x1) < abs(x2):
        return x1

    return x2
