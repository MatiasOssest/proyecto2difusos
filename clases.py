# -*- coding: utf-8 -*-

class Sistema:
    ALPHA = 0.7
    BETA = 0.2
    GAMMA = 0.85
    EPSILON = 0.5
    DELTA = lambda vc: 0.2 / vc

    def __init__(self, base_hechos, base_reglas, hipotesis, d1=True):
        self.d1 = d1
        self.base_hechos = base_hechos
        self.base_reglas = base_reglas
        self.hipotesis = hipotesis

    def __str__(self):
        string = "Base de Hechos: %s \nBase de Reglas: %s \n hipotesis: %s" % \
                 (self.base_hechos, self.base_reglas, self.hipotesis)
        return string

    def preguntar(self, pregunta):
        respuesta = input(pregunta[0])
        premisa = pregunta[1]
        hecho = Hecho(premisa, respuesta)
        self.evaluar(hecho)

    def evaluar(self, hecho):
        '''
        1.- Revisa la base de hechos si es que una hipótesis cumple cierto valor de certeza
        2.- Revisa la base de reglas, cuales se activan y actualiza las hipótesis
        3.- Se almacenan las hipótesis actualizadas en la base de Hechos.
        :param hecho:
        :return: None
        '''
        pass


class BaseHecho:

    def __init__(self, *args):
        self.hechos = []
        for hecho in args:
            self.hechos.append(hecho)

    def __str__(self):
        string = "["
        for idx, hecho in enumerate(self.hechos):
            string += str(hecho)
            if idx < len(self.hechos) - 1:
                string += ', '
        string += "]"
        return string

    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)

    def reset_vc(self):
        for hecho in self.hechos:
            hecho.vc = 0.0


class Hecho:

    def __init__(self, tripleta, vc):
        self.tripleta = tripleta
        self.vc = vc

    def __str__(self):
        return "(" + str(self.tripleta) + " " + str(self.vc) + ")"


class Tripleta:

    def __init__(self, obj, atr, val):
        self.obj = obj
        self.atr = atr
        self.val = val

    def __str__(self):
        return "(%s %s %s)" % (self.obj, self.atr, self.val)

    def equal(self, t2):
        return self.obj == t2.obj and self.atr == t2.atr and self.val == t2.val


class BaseReglas:

    def __init__(self):
        self.reglas = []

    def __str__(self):
        string = ""
        for regla in self.reglas:
            string += "%s \n" % str(regla)
        return string

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def get_regla(self, identif):
        for regla in self.reglas:
            if regla.identif == identif:
                return regla

    def keys(self):
        key = []
        for regla in self.reglas:
            key.append(regla.identif)
        return key


class Regla:

    def __init__(self, identif, premisa, conclusion):
        self.identif = identif
        self.premisa = premisa
        self.conclusion = conclusion

    def __str__(self):
        string = "(%s : " % self.identif
        string += str(self.premisa) + "\n"
        string += "      %s)" % str(self.conclusion)
        return string


class Premisa:

    def __init__(self, *tripletas):
        self.clausula = []
        for tripleta in tripletas:
            self.clausula.append(tripleta)

    def __str__(self):
        string = "["
        for idx, tripleta in enumerate(self.clausula):
            string += str(tripleta)
            if idx < len(self.clausula) - 1:
                string += ", "
        string += "]"
        return string
