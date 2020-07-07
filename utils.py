def disyuncion(x1):
    mayor = -2
    for valor in x1:
        if abs(valor) > abs(mayor):
            mayor = valor
    return mayor


def conjuncion(x1):
    menor = 2
    for valor in x1:
        if abs(valor) < abs(menor):
            menor = valor
    return menor


def producto(vc):
    prod = 1
    for valor in vc:
        prod = prod * valor
    return prod


def obtener_clases(preguntas):
    clases = {}
    for pregunta in preguntas:

        try:
            clase = pregunta["clase"]
            if clase and clase not in clases:
                clases[clase] = False
        except:
            pass

    return clases
