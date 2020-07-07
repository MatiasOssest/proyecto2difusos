# -*- coding: utf-8 -*-
import json
from utils import *


class Sistema:
    ALPHA = 0.7
    BETA = 0.2
    GAMMA = 0.85
    EPSILON = 0.5
    DELTA = lambda vc: 0.2 / vc

    with open("preguntas.json", encoding="utf-8") as f:
        preguntas = json.load(f)

    def __init__(self, base_hechos, base_reglas, hipotesis, d1=True):
        self.d1 = d1
        self.base_hechos = base_hechos
        self.base_reglas = base_reglas
        self.hipotesis = hipotesis
        self.clases = obtener_clases(self.preguntas)

    def __str__(self):
        string = "Base de Hechos: %s \nBase de Reglas: %s \n hipotesis: %s" % \
                 (self.base_hechos, self.base_reglas, self.hipotesis)
        return string

    def evaluar(self):
        '''
        1.- Revisa la base de hechos si es que una hipótesis o conclusion intermedia
            cumple cierto valor de certeza, si no está, se realiza una pregunta y se evalúa
            el hecho en la base de reglas
        2.- Revisa la base de reglas, cuales se activan y actualiza las hipótesis
        3.- Se almacenan las hipótesis actualizadas en la base de Hechos.
        :param hecho:
        :return: None
        '''
        self.pregunta = self.get_pregunta()

        for hipo in self.hipotesis:
            self.revisar_base_hechos(hipo)
            if hipo.vc >= self.ALPHA:
                print(self.hipotesis)
                break

    def revisar_base_hechos(self, hipo):
        conclusiones_int = self.get_conclusion_intermedia(hipo)
        for conclu in conclusiones_int:
            esta_o_importante = self.base_hechos.es_importante(conclu, self.GAMMA)
            # la conclusión intermedia no se puede obtener de las reglas
            if conclu.special:
                hecho = self.pregunta_especial(conclu)
                self.base_hechos.agregar_hecho(hecho)
            # si la conclusión intermedia no está en la base de hechos o no tiene
            # suficiente importancia para seguir mejorando, hacer una pregunta

            elif not esta_o_importante:
                hecho = Hecho(conclu, 0)
                self.base_hechos.agregar_hecho(hecho)
                while abs(hecho.vc) <= self.GAMMA:
                    #try:
                    respuesta = self.preguntar()
                    self.base_hechos.agregar_hecho(respuesta)
                    print(self.base_hechos)
                    self.evaluar_reglas()
                    hecho = self.base_hechos.buscar(conclu)

                    #except:
                     #   print("No hay más preguntas, los resultados son: \n%s"%self.hipotesis)
                      #  break

    def evaluar_reglas(self):

        for regla in self.base_reglas:
            mis_vc = [] # según las premisas de la reglas se consideran sus vc
            for p in regla.premisa:
                hecho = self.base_hechos.buscar(p)
                print(hecho)
                mis_vc.append(hecho.vc)

            print(mis_vc)
            minimo = conjuncion(mis_vc)
            print(minimo)
            if minimo > 0.2:
                for conclu in regla.conclusion:
                    h = Hecho(conclu.tripleta, conclu.vc*minimo)
                    self.base_hechos.reemplazar(h)

    def pregunta_especial(self, tripleta):
        res = float(input("¿El %s %s %s ? : \n" % (tripleta.obj, tripleta.atr, tripleta.val)))
        return Hecho(tripleta, res)

    def preguntar(self):
        p = next(self.pregunta)
        if self.clases[p["clase"]]:
            respuesta = -1
        else:
            respuesta = float(input(p["pregunta"] + " : \n"))

        premisa = Tripleta(p["obj"], p["atr"], p["val"])
        return Hecho(premisa, respuesta)

    def get_pregunta(self):
        for preg in self.preguntas:
            yield preg

    def get_conclusion_intermedia(self, hipo):
        for regla in self.base_reglas:
            if str(regla.conclusion[0].tripleta) == str(hipo.tripleta):
                return regla.premisa

    def menor(self):
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

    def __getitem__(self, item):
        return self.hechos[item]

    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)

    def reset_vc(self):
        for hecho in self.hechos:
            hecho.vc = 0.0

    def get_last(self):
        return self.hechos[-1]

    def esta_en_la_base(self, tripleta):
        for hecho in self.hechos:
            if hecho.tripleta.equal(tripleta):
                return True

        return False

    def buscar(self, tripleta):
        for hecho in self.hechos:
            if hecho.tripleta.equal(tripleta):
                return hecho
        return Hecho(tripleta, 0)

    def reemplazar(self, hecho):
        for idx, h in enumerate(self.hechos):
            if not self.esta_en_la_base(hecho):
                self.agregar_hecho(hecho)
                break
            elif h.equals(hecho) and abs(h.vc) <= abs(hecho.vc):
                self.hechos[idx] = hecho
                break

    def es_importante(self, tripleta, threshold):
        if self.esta_en_la_base(tripleta):
            hecho = self.buscar(tripleta)
            return hecho.vc >= threshold
        return False

class Hecho:

    def __init__(self, tripleta, vc):
        self.tripleta = tripleta
        self.vc = vc

    def __str__(self):
        return "(" + str(self.tripleta) + " " + str(self.vc) + ")"

    def equals(self, h):
        return self.tripleta.equal(h.tripleta)

class Tripleta:

    def __init__(self, obj, atr, val, special=False):
        self.obj = obj
        self.atr = atr
        self.val = val
        self.special = special

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

    def __getitem__(self, item):
        return self.reglas[item]

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

    def __getitem__(self, item):
        return self.clausula[item]
