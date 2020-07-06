# -*- coding: utf-8 -*-

# Proyecto 2 Sistemas Difusos
# Profesor: Claudio Held
# Auxiliar: Leonardo Causa
# Estudiante: Matías Osses
# Estudiante: Alvaro Toledo

import json

from objetos import base_de_reglas, base_de_hechos, hipotesis
from clases import *
from utils import *


sistema = Sistema(base_de_hechos, base_de_reglas, hipotesis)

with open("preguntas.json", encoding="utf-8") as f:
    preguntas = json.load(f)


def generaPreguntas(pregs):
    for pregunta in pregs:
        yield pregunta

p = generaPreguntas(preguntas)
print(next(p))
clases = obtener_clases(preguntas)


sistema.base_hechos.agregar_hecho(hipotesis)

a = sistema.get_conclusion_intermedia(hipotesis[0])

print(type(sistema.base_reglas[0].premisa[0]))