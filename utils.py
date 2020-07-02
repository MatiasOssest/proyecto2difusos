def disyuncion(x1, x2):
    if abs(x1) > abs(x2):
        return x1

    return x2


def conjuncion(x1, x2):
    if abs(x1) < abs(x2):
        return x1

    return x2

def obtener_clases(preguntas):
    clases={}
    for pregunta in preguntas:

        try:
            clase = pregunta["clase"]
            if clase and clase not in clases:
                clases[clase] = False
        except:
            pass

    return clases
